  var tabs = document.querySelectorAll('[id^="tabs-"]');

  const setElementAttributes = {
      class: 'nav-link active',
  };
  const releaseElementAttributes = {
      class: 'nav-link',
  };

  function setMultipleAttributesonElement(elem, setElementAttributes) {
      Object.keys(setElementAttributes).forEach(attribute => {
          elem.setAttribute(attribute, setElementAttributes[attribute]);
      });

  }

  
  for (let index = 0; index < tabs.length; index++) {
      const element = tabs[index].addEventListener(
      "click",
      function () {
          if (tabs[index].id == 'tabs-description-' + tabs[index].getAttribute("num")) {
              document.getElementById("tab_description-" + tabs[index].getAttribute("num")).hidden = false;
              document.getElementById("tab_architecture-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_features-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_sources-" + tabs[index].getAttribute("num")).hidden = true;
              
              const r_description_lnk = document.getElementById(tabs[index].id);
              const r_architecture_lnk = document.getElementById("tabs-architecture-" + tabs[index].getAttribute("num"));
              const r_features_lnk = document.getElementById("tabs-features-" + tabs[index].getAttribute("num"));
              const r_r_lnk = document.getElementById("tabs-sources-" + tabs[index].getAttribute("num"));

              setMultipleAttributesonElement(r_description_lnk, setElementAttributes);

              setMultipleAttributesonElement(r_architecture_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_features_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_sources_lnk, releaseElementAttributes);

          } else if (tabs[index].id == 'tabs-architecture-' + tabs[index].getAttribute("num")) {
              document.getElementById("tab_description-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_features-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_architecture-" + tabs[index].getAttribute("num")).hidden = false;
              document.getElementById("tab_sources-" + tabs[index].getAttribute("num")).hidden = true;
              
              const r_description_lnk = document.getElementById("tabs-description-" + tabs[index].getAttribute("num"));
              const r_architecture_lnk = document.getElementById(tabs[index].id);
              const r_features_lnk = document.getElementById("tabs-features-" + tabs[index].getAttribute("num"));
              const r_sources_lnk = document.getElementById("tabs-sources-" + tabs[index].getAttribute("num"));

              setMultipleAttributesonElement(r_description_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_architecture_lnk, setElementAttributes);
              setMultipleAttributesonElement(r_features_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_sources_lnk, releaseElementAttributes);

          }else if (tabs[index].id == 'tabs-features-' + tabs[index].getAttribute("num")) {
              document.getElementById("tab_description-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_features-" + tabs[index].getAttribute("num")).hidden = false;
              document.getElementById("tab_architecture-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_sources-" + tabs[index].getAttribute("num")).hidden = true;
              
              const r_description_lnk = document.getElementById("tabs-description-" + tabs[index].getAttribute("num"));
              const r_architecture_lnk = document.getElementById("tabs-architecture-" + tabs[index].getAttribute("num"));
              const r_features_lnk = document.getElementById(tabs[index].id);
              const r_sources_lnk = document.getElementById("tabs-r-" + tabs[index].getAttribute("num"));

              setMultipleAttributesonElement(r_description_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_architecture_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_features_lnk, setElementAttributes);
              setMultipleAttributesonElement(r_sources_lnk, releaseElementAttributes);

          }else if (tabs[index].id == 'tabs-sources-' + tabs[index].getAttribute("num")) {
              document.getElementById("tab_description-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_features-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_architecture-" + tabs[index].getAttribute("num")).hidden = true;
              document.getElementById("tab_sources-" + tabs[index].getAttribute("num")).hidden = false;
              
              const r_description_lnk = document.getElementById("tabs-description-" + tabs[index].getAttribute("num"));
              const r_architecture_lnk = document.getElementById("tabs-architecture-" + tabs[index].getAttribute("num"));
              const r_features_lnk = document.getElementById("tabs-features-" + tabs[index].getAttribute("num"));
              const r_sources_lnk = document.getElementById(tabs[index].id);

              setMultipleAttributesonElement(r_description_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_architecture_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_features_lnk, releaseElementAttributes);
              setMultipleAttributesonElement(r_sources_lnk, setElementAttributes);

          }
              
      });
  };
