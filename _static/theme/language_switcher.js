const initLanguageSwitcher = () => {
  const languages = []

  $('.rst-other-versions dt:contains(Languages)')
    .siblings('dd')
    .each((_index, item) => {
      languages.push({
        id: $(item).text().trim(),
        url: $(item).find('a').attr('href'),
        isCurrent: $(item).hasClass('rtd-current-item'),
      })
    })

  if (!languages.length) return

  const switcherIcon = $('<i />')
    .addClass('fa fa-language')

  const switcherLabel = $('<label />')
    .attr('for', 'language-switcher')
    .prepend(switcherIcon)
    .prepend(switcherIcon)

  const switcherOptions = languages.map((language) =>
    $('<option />')
      .attr('value', language.url)
      .text(language.id)
      .attr('selected', language.isCurrent)
  )

  const switcherSelection = $('<select />')
    .attr('id', 'language-switcher')
    .prepend(switcherOptions)
    .off('change.language')
    .on('change.language', (e) => {
      location.href = $(e.target).val()
    })

  const switcher = $('<li />')
    .addClass('zammad-language-switcher wy-breadcrumbs-aside')
    .prepend(switcherSelection)
    .prepend(switcherLabel)

  $('.wy-breadcrumbs-aside').before(switcher)
}

$(document).ready(() => {
  const intervalId = setInterval(() => {
    if (!$('.rst-other-versions dt:contains(Languages)').length) return
    clearInterval(intervalId);
    initLanguageSwitcher()
  }, 100)
})
