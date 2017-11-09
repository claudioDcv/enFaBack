var serializeForm = function(form, opt) {
    if (!form || form.nodeName !== "FORM") {
        return;
    }

    var enc = function(data){
      if (opt) {
        if (opt.encodeURIComponent) {
          return encodeURIComponent(data);
        }
      }
      return data;
    }

    var i, j,
        obj = {};
    for (i = form.elements.length - 1; i >= 0; i = i - 1) {
        if (form.elements[i].name === "") {
            continue;
        }
        switch (form.elements[i].nodeName) {
            case 'INPUT':
                switch (form.elements[i].type) {
                    case 'text':
                    case 'hidden':
                    case 'password':
                    case 'button':
                    case 'reset':
                    case 'submit':
                        obj[form.elements[i].name] = enc(form.elements[i].value);
                        break;
                    case 'checkbox':
                    case 'radio':
                        if (form.elements[i].checked) {
                            obj[form.elements[i].name] = enc(form.elements[i].value);
                        }
                        break;
                    case 'file':
                        break;
                }
                break;
            case 'TEXTAREA':
                obj[form.elements[i].name] = enc(form.elements[i].value);
                break;
            case 'SELECT':
                switch (form.elements[i].type) {
                  case 'select-one':
                      obj[form.elements[i].name] = enc(form.elements[i].value);
                      break;
                  case 'select-multiple':
                      obj[form.elements[i].name] = []
                      for (j = form.elements[i].options.length - 1; j >= 0; j = j - 1) {
                          if (form.elements[i].options[j].selected) {
                              obj[form.elements[i].name].push(enc(form.elements[i].options[j].value));
                          }
                      }
                      break;
                }
                break;
            case 'BUTTON':
                switch (form.elements[i].type) {
                    case 'reset':
                    case 'submit':
                    case 'button':
                        obj[form.elements[i].name] = enc(form.elements[i].value);
                        break;
                }
                break;
        }
    }
    return obj;
}


var select2 = function(elm, url, remap) {
  var $elm = $(elm);
  if ($elm) {
    $elm.select2({
      multiple: true,
      ajax: {
        url: url,
        dataType: 'json',
        processResults: function (data) {
        // Tranforms the top-level key of the response object from 'items' to 'results'
          return {
            results: data.map(remap)
          };
        }
        // Additional AJAX parameters go here; see the end of this chapter for the full code of this example
      }
    });
  }
}

select2('#id_musical_styles', '/api/musical-styles/',function(e) {
  return {
    id: e.id,
    text: e.name,
  };
});
select2('#id_permanent_musician', '/api/users-musical-instrument-style/',function(e) {
  return {
    id: e.id,
    text: e.user.username,
  };
});
select2('#id_guest_musician', '/api/users-musical-instrument-style/',function(e) {
  return {
    id: e.id,
    text: e.user.username,
  };
});



var ajaxForms = document.querySelectorAll('form.ajax-form');

ajaxForms.forEach(function(e){
  e.addEventListener('submit', event => {
    event.preventDefault()
    var url = event.target.action;
    var data = serializeForm(event.target);
    data.creation_date = data.creation_date.split("/").reverse().join("-");
    var successUrl = event.target.dataset.success;
    console.log(url);
    console.log(serializeForm(event.target));
        $.ajax({
        type: "patch",
        url: url,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        headers: {
          'X-CSRFToken': data.csrfmiddlewaretoken,
        },
        data: JSON.stringify(data),
        success: function(result) {
            console.log(result);
            window.location.href = successUrl;
        }
    });
  }, false)
})




window.addEventListener('DOMContentLoaded', function()
        {
            var $min = document.querySelector('.datepicker');
            if ($min) {
              // $max = document.querySelector('.real [name="realDPX-max"]');
              $min.DatePickerX.init({
                  mondayFirst: true,
                  // minDate    : new Date(2017, 8, 13),
                  format: 'dd/mm/yyyy',
                  // maxDate    : $max
              });
              // $max.DatePickerX.init({
              //     mondayFirst: true,
              //     minDate    : $min,
              //     //maxDate    : new Date(2017, 4, 25)
              // });
            }

            if (document.querySelector('[name="duration"]')) {
              window.picker = new JsTimepicker(document.querySelector('[name="duration"]'), {
                hourLeadingZero: true,
                hourStep: 1,
                minuteLeadingZero: true,
                minuteStep: 1,
              });
            }
        });
