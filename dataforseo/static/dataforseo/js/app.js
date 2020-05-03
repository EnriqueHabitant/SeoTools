// Seleccionar por defecto es/ES en el selector de idiomas.
document.querySelectorAll('#id_language option').forEach((e) => e.text === 'es/ES' ? e.selected = true : '')

// Petición a la API dataforseo y registro del resultado en la BBDD.
document.querySelector('#send_keywordFinder').addEventListener('click', async () => {
  event.preventDefault()
  document.querySelector('#id_user').value = document.querySelector('#user').value
  const form = document.querySelector('#keywordFinder')
  const dataForm = new FormData(form)
  const lang = dataForm.get('language').split('/')
  // const loading = document.querySelector('#is-loading')
  // loading.classList.toggle('is-active')
  // Comprobación si tenemos o no Filtros
  const filters = getFilters() === '' ? 'False' : getFilters()

  // isLoading();

  // /keyword-search/related_keywords/[KEYWORD]/[COUNTRY_CODE]/[LANGUAGE_CODE]/[DEPTH]/[LIMIT]/
  const url = `/keyword-research/keyword-finder/${dataForm.get('keyword')}/${lang[0]}/${lang[1]}/${dataForm.get('depth')}/${dataForm.get('limit')}/${filters}`
  await fetch(url)
    .then(data => data.json())
    .then(data => {
      form.querySelector('#id_result').value = JSON.stringify(data)
    })
    .then(() => form.submit())
})

/**
 * Añadir filtro (fila)
 */
function addFilter(target) {
  const fileUrl = '/keyword-research/includes/filter/' // provide file location

  fetch(fileUrl)
    .then(r => r.text())
    .then(aChild => {
      target.parentNode.appendChild(document.createElement('p'))
      target.parentNode.querySelector('p').outerHTML = aChild
    })
}

/**
 * Eliminar filtro (fila)
 */
function removeFilter(target) {
  target.parentNode.remove()
}

/**
 * Agrupar filtros para la petición a la API
 */
function getFilters() {
  const filtersGroup = document.querySelectorAll(".js-filters-group")
  const idFilter = document.querySelector('#id_filters')
  const filters = []

  filtersGroup.forEach(grupo => {
    grupo.querySelectorAll('.js-filter').forEach(e => {
      const filtro = []
      const field = e.querySelector('.js-field').value;
      const operator = e.querySelector('.js-operator').value;
      let valueFilter = e.querySelector('.js-value').value;

      if (field === 'key') valueFilter = `%${valueFilter}%`

      filtro.push(field, operator, valueFilter)
      filters.push(filtro)
    })
  })

  idFilter.value = filters.join('&&')
  return idFilter.value
}

/**
 * Cambiar el valor del campo operador
 */
function changeOperators(target) {
  const operators = { key: [['like', 'contiene'], ['not_like', 'no contiene']], other: [['<', 'menor que'], ['<=', 'menor igual que'], ['>', 'mayor que'], ['>=', 'mayor igual que'], ['=', 'igual que'], ['<>', 'diferente que']] }
  const field = target.parentNode.parentNode.querySelector('.js-operator')

  if (target.value === "key") {
    field.innerHTML = ""
    operators.key.map(e => field.innerHTML += `<option value="${e[0]}">${e[1]}</option>`)
  } else {
    field.innerHTML = ""
    operators.other.map(e => field.innerHTML += `<option value="${e[0]}">${e[1]}</option>`)
  }
}

/**
 * Alternar selected
 */
const toggleSelected = (target) => target.classList.toggle('is-selected')
/**
 * Copiar tablas seleccionadas
 */
function copySelectedRows(target) {
  const padre = target.parentNode.parentNode
  const table = target.parentNode.parentNode.querySelector('tbody')

  console.log(padre)

  padre.appendChild(document.createElement('textarea'))
  const textArea = padre.querySelector('textarea')
  table.querySelectorAll('tr').forEach(row => {
    return row.classList.value === 'is-selected' ? textArea.value = `${textArea.value + row.innerText}\n` : ''
  })

  // Seleccionar Valor
  textArea.select();
  // Copia el texto seleccionado
  document.execCommand("copy");
  // Elimina el campo de la página
  textArea.remove();
}
/**
 * Copiar todas las filas de la tabla
 */
function copyAllRows(target) {
  const padre = target.parentNode.parentNode
  const table = target.parentNode.parentNode.querySelector('tbody')

  padre.appendChild(document.createElement('textarea'))
  const textArea = padre.querySelector('textarea')
  table.querySelectorAll('tr').forEach(row => textArea.value = `${textArea.value + row.innerText}\n`)

  // Seleccionar Valor
  textArea.select();
  // Copia el texto seleccionado
  document.execCommand("copy");
  // Elimina el campo de la página
  textArea.remove();
}

/**
 * Mostrar siguiente tabla de resultados
 */
document.querySelector('.js-tabs').addEventListener('click', (object) => {
  idTab = object.target.parentNode.id
  tab = object.target.parentNode

  if (tab.classList[0] === 'o-tabs__items') {
    document.querySelectorAll('.js-tabs .o-tabs__items').forEach(e => {
      e.id === idTab ? e.classList.add('is-selected') : e.classList.remove('is-selected')
    })
  
    document.querySelectorAll('.c-table').forEach(e => {
      e.id === (`table-${idTab}`) ? e.classList.add('is-active') : e.classList.remove('is-active')
    })
  }

})

/**
 * Carga de modal Loading
 */
function isLoading() {
  const fileUrl = '/keyword-research/includes/loading/' // provide file location

  fetch(fileUrl)
    .then(r => r.text())
    .then(aChild => {
      document.body.outerHTML += aChild
    })
}