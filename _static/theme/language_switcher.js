const initLanguageSwitcher = () => {
  const languages = []

  const languagesList = $('.rst-other-versions dt').eq(0)
  const languagesLabel = languagesList.text()

  languagesList.siblings('dd')
    .each((_index, item) => {
      languages.push({
        id: $(item).text().trim(),
        url: $(item).find('a').attr('href'),
        isCurrent: $(item).hasClass('rtd-current-item'),
      })
    })

  if (!languages.length) return

  const switcherIcon = $('<i />')
    .addClass('fa fa-lg fa-language')

  const switcherLabel = $('<label />')
    .attr('for', 'language-switcher')
    .prepend(switcherIcon)
    .prepend(switcherIcon)

  const switcherLanguageOptions = languages.map((language) =>
    $('<option />')
      .attr('value', language.url)
      .text(language.id)
      .attr('selected', language.isCurrent)
  )

  const switcherLanguageOptionsGroup = $('<optgroup />')
    .attr('label', languagesLabel)
    .html(switcherLanguageOptions)

  const switcherContributeOption = $('<option />')
    .attr('value', 'https://docs.zammad.org/en/latest/contributing/start.html')
    .text('Contribute translation')

  const switcherContributeOptionGroup = $('<optgroup />')
    .attr('label', 'Missing language?')
    .html(switcherContributeOption)

  const switcherSelection = $('<select />')
    .attr('id', 'language-switcher')
    .append(switcherLanguageOptionsGroup)
    .append(switcherContributeOptionGroup)
    .off('change.language')
    .on('change.language', (e) => {
      location.href = $(e.target).val()
    })

  $('.wy-breadcrumbs-aside')
    .addClass('zammad-language-switcher')
    .append(switcherLabel)
    .append(switcherSelection)
}

$(document).ready(() => {
  const intervalId = setInterval(() => {
    if ($('.rst-other-versions dt').length !== 6) return
    clearInterval(intervalId);
    initLanguageSwitcher()
  }, 100)
})
