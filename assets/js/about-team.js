$(".option").click(function(){
   $(".option").removeClass("active");
   $(this).addClass("active");
   
});

$("section#map .container").mapael({
    map : {
        name : "world_countries",
        defaultArea: {
            attrs: {
                "fill": "#00b3f7",
                "stroke": "#013f57",
                "stroke-width": 2
            },
            attrsHover: {
                "fill": "#1abeff",
                "stroke-width": 2
            }
        }
    },
    legend: {
        area: {
            title: "Members in countries",
            slices: [
                {
                    max: 1,
                    attrs: {
                        fill: "#0092cc"
                    },
                    legendSpecificAttrs: {
                        stroke: '#013f57',
                        "stroke-width": 2,
                        width: 50,
                        height: 50
                    },
                    label: "Less than 2 members"
                },
                {
                    min: 2,
                    max: 5,
                    attrs: {
                        fill: "#006e99"
                    },
                    legendSpecificAttrs: {
                        stroke: '#013f57',
                        "stroke-width": 2,
                        width: 50,
                        height: 50
                    },
                    label: "Between 2 and 5 members"
                },
                {
                    min: 6,
                    attrs: {
                        fill: "#004966"
                    },
                    legendSpecificAttrs: {
                        stroke: '#013f57',
                        "stroke-width": 2,
                        width: 50,
                        height: 50
                    },
                    label: "More than 6 members"
                }
            ]
        }
    },
    areas: {
        /*"AF": {
            "value": "0",
            "attrs": {
                "href": "#"
            },
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Afghanistan<\/span>"
            }
        },
        "ZA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">South Africa<\/span>"
            }
        },
        "AL": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Albania<\/span>"
            }
        },
        "DZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Algeria<\/span>"
            }
        },
        "DE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Germany<\/span>"
            }
        },
        "AD": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Andorra<\/span>"
            }
        },
        "AO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Angola<\/span>"
            }
        },
        "AG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Antigua And Barbuda<\/span>"
            }
        },
        "SA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Saudi Arabia<\/span>"
            }
        },
        "AR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Argentina<\/span>"
            }
        },
        "AM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Armenia<\/span>"
            }
        },
        "AU": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Australia<\/span>"
            }
        },
        "AT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Austria<\/span>"
            }
        },
        "AZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Azerbaijan<\/span>"
            }
        },
        "BS": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Bahamas<\/span>"
            }
        },
        "BH": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Bahrain<\/span>"
            }
        },
        "BD": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Bangladesh<\/span>"
            }
        },
        "BB": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Barbados<\/span>"
            }
        },
        "BE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Belgium<\/span>"
            }
        },
        "BZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Belize<\/span>"
            }
        },
        "BJ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Benin<\/span>"
            }
        },
        "BT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Bhutan<\/span>"
            }
        },
        "BY": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Belarus<\/span>"
            }
        },
        "MM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Myanmar<\/span>"
            }
        },
        "BO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Bolivia, Plurinational State Of<\/span>"
            }
        },
        "BA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Bosnia And Herzegovina<\/span>"
            }
        },
        "BW": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Botswana<\/span>"
            }
        },
        "BR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Brazil<\/span>"
            }
        },
        "BN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Brunei Darussalam<\/span>"
            }
        },
        "BG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Bulgaria<\/span>"
            }
        },
        "BF": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Burkina Faso<\/span>"
            }
        },
        "BI": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Burundi<\/span>"
            }
        },
        "KH": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Cambodia<\/span>"
            }
        },
        "CM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Cameroon<\/span>"
            }
        },
        "CA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Canada<\/span>"
            }
        },
        "CV": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Cape Verde<\/span>"
            }
        },
        "CF": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Central African Republic<\/span>"
            }
        },
        "CL": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Chile<\/span>"
            }
        },
        "CN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">China<\/span>"
            }
        },
        "CY": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Cyprus<\/span>"
            }
        },
        "CO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Colombia<\/span>"
            }
        },
        "KM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Comoros<\/span>"
            }
        },
        "CG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Congo<\/span>"
            }
        },
        "CD": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Congo, The Democratic Republic Of The<\/span>"
            }
        },
        "KP": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Korea, Democratic People's Republic Of<\/span>"
            }
        },
        "KR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Korea, Republic Of<\/span>"
            }
        },
        "CR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Costa Rica<\/span>"
            }
        },
        "CI": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">C\u00d4te D'ivoire<\/span>"
            }
        },
        "HR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Croatia<\/span>"
            }
        },
        "CU": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Cuba<\/span>"
            }
        },
        "DK": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Denmark<\/span>"
            }
        },
        "DJ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Djibouti<\/span>"
            }
        },
        "DM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Dominica<\/span>"
            }
        },
        "EG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Egypt<\/span>"
            }
        },
        "AE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">United Arab Emirates<\/span>"
            }
        },
        "EC": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Ecuador<\/span>"
            }
        },
        "ER": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Eritrea<\/span>"
            }
        },
        "ES": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Spain<\/span>"
            }
        },
        "EE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Estonia<\/span>"
            }
        },*/
        "US": {
            "value": "3",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">United States<\/span>"
            }
        },
        /*"ET": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Ethiopia<\/span>"
            }
        },
        "FJ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Fiji<\/span>"
            }
        },*/
        "FI": {
            "value": "1",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Finland<\/span>"
            }
        },
        /*"FR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">France<\/span>"
            }
        },
        "GA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Gabon<\/span>"
            }
        },
        "GM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Gambia<\/span>"
            }
        },
        "GE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Georgia<\/span>"
            }
        },
        "GH": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Ghana<\/span>"
            }
        },
        "GR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Greece<\/span>"
            }
        },
        "GD": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Grenada<\/span>"
            }
        },
        "GT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Guatemala<\/span>"
            }
        },
        "GN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Guinea<\/span>"
            }
        },
        "GQ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Equatorial Guinea<\/span>"
            }
        },
        "GW": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Guinea-bissau<\/span>"
            }
        },
        "GY": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Guyana<\/span>"
            }
        },
        "HT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Haiti<\/span>"
            }
        },
        "HN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Honduras<\/span>"
            }
        },
        "HU": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Hungary<\/span>"
            }
        },
        "JM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Jamaica<\/span>"
            }
        },
        "JP": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Japan<\/span>"
            }
        },
        "MH": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Marshall Islands<\/span>"
            }
        },
        "PW": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Palau<\/span>"
            }
        },
        "SB": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Solomon Islands<\/span>"
            }
        },*/
        "IN": {
            "value": "1",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">India<\/span>"
            }
        },
        /*"ID": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Indonesia<\/span>"
            }
        },
        "JO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Jordan<\/span>"
            }
        },
        "IR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Iran, Islamic Republic Of<\/span>"
            }
        },
        "IQ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Iraq<\/span>"
            }
        },
        "IE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Ireland<\/span>"
            }
        },
        "IS": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Iceland<\/span>"
            }
        },
        "IL": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Israel<\/span>"
            }
        },
        "IT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Italy<\/span>"
            }
        },
        "KZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Kazakhstan<\/span>"
            }
        },
        "KE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Kenya<\/span>"
            }
        },
        "KG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Kyrgyzstan<\/span>"
            }
        },
        "KI": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Kiribati<\/span>"
            }
        },
        "KW": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Kuwait<\/span>"
            }
        },
        "LA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Lao People's Democratic Republic<\/span>"
            }
        },
        "LS": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Lesotho<\/span>"
            }
        },
        "LV": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Latvia<\/span>"
            }
        },
        "LB": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Lebanon<\/span>"
            }
        },
        "LR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Liberia<\/span>"
            }
        },
        "LY": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Libya<\/span>"
            }
        },
        "LI": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Liechtenstein<\/span>"
            }
        },
        "LT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Lithuania<\/span>"
            }
        },
        "LU": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Luxembourg<\/span>"
            }
        },
        "MK": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Macedonia, The Former Yugoslav Republic Of<\/span>"
            }
        },
        "MG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Madagascar<\/span>"
            }
        },
        "MY": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Malaysia<\/span>"
            }
        },
        "MW": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Malawi<\/span>"
            }
        },
        "MV": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Maldives<\/span>"
            }
        },
        "ML": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Mali<\/span>"
            }
        },
        "MT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Malta<\/span>"
            }
        },
        "MA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Morocco<\/span>"
            }
        },
        "MU": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Mauritius<\/span>"
            }
        },
        "MR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Mauritania<\/span>"
            }
        },
        "MX": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Mexico<\/span>"
            }
        },
        "FM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Micronesia, Federated States Of<\/span>"
            }
        },
        "MD": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Moldova, Republic Of<\/span>"
            }
        },
        "MC": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Monaco<\/span>"
            }
        },
        "MN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Mongolia<\/span>"
            }
        },
        "ME": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Montenegro<\/span>"
            }
        },
        "MZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Mozambique<\/span>"
            }
        },
        "NA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Namibia<\/span>"
            }
        },
        "NP": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Nepal<\/span>"
            }
        },
        "NI": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Nicaragua<\/span>"
            }
        },
        "NE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Niger<\/span>"
            }
        },
        "NG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Nigeria<\/span>"
            }
        },
        "NO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Norway<\/span>"
            }
        },
        "NZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">New Zealand<\/span>"
            }
        },
        "OM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Oman<\/span>"
            }
        },
        "UG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Uganda<\/span>"
            }
        },
        "UZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Uzbekistan<\/span>"
            }
        },
        "PK": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Pakistan<\/span>"
            }
        },
        "PS": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Palestine, State Of<\/span>"
            }
        },
        "PA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Panama<\/span>"
            }
        },
        "PG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Papua New Guinea<\/span>"
            }
        },
        "PY": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Paraguay<\/span>"
            }
        },
        "NL": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Netherlands<\/span>"
            }
        },
        "PE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Peru<\/span>"
            }
        },
        "PH": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Philippines<\/span>"
            }
        },
        "PL": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Poland<\/span>"
            }
        },
        "PT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Portugal<\/span>"
            }
        },
        "QA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Qatar<\/span>"
            }
        },
        "DO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Dominican Republic<\/span>"
            }
        },
        "RO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Romania<\/span>"
            }
        },
        "GB": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">United Kingdom<\/span>"
            }
        },
        "RU": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Russian Federation<\/span>"
            }
        },
        "RW": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Rwanda<\/span>"
            }
        },
        "KN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Saint Kitts And Nevis<\/span>"
            }
        },
        "SM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">San Marino<\/span>"
            }
        },
        "VC": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Saint Vincent And The Grenadines<\/span>"
            }
        },
        "LC": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Saint Lucia<\/span>"
            }
        },
        "SV": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">El Salvador<\/span>"
            }
        },
        "WS": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Samoa<\/span>"
            }
        },
        "ST": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Sao Tome And Principe<\/span>"
            }
        },
        "SN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Senegal<\/span>"
            }
        },
        "RS": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Serbia<\/span>"
            }
        },
        "SC": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Seychelles<\/span>"
            }
        },
        "SL": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Sierra Leone<\/span>"
            }
        },
        "SG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Singapore<\/span>"
            }
        },
        "SK": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Slovakia<\/span>"
            }
        },
        "SI": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Slovenia<\/span>"
            }
        },
        "SO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Somalia<\/span>"
            }
        },
        "SD": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Sudan<\/span>"
            }
        },
        "SS": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">South Sudan<\/span>"
            }
        },
        "LK": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Sri Lanka<\/span>"
            }
        },
        "SE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Sweden<\/span>"
            }
        },
        "CH": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Switzerland<\/span>"
            }
        },
        "SR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Suriname<\/span>"
            }
        },
        "SZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Swaziland<\/span>"
            }
        },
        "SY": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Syrian Arab Republic<\/span>"
            }
        },
        "TJ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Tajikistan<\/span>"
            }
        },
        "TZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Tanzania, United Republic Of<\/span>"
            }
        },
        "TD": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Chad<\/span>"
            }
        },
        "CZ": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Czech Republic<\/span>"
            }
        },
        "TH": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Thailand<\/span>"
            }
        },
        "TL": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Timor-leste<\/span>"
            }
        },
        "TG": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Togo<\/span>"
            }
        },
        "TO": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Tonga<\/span>"
            }
        },
        "TT": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Trinidad And Tobago<\/span>"
            }
        },
        "TN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Tunisia<\/span>"
            }
        },
        "TM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Turkmenistan<\/span>"
            }
        },
        "TR": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Turkey<\/span>"
            }
        },
        "TV": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Tuvalu<\/span>"
            }
        },
        "VU": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Vanuatu<\/span>"
            }
        },
        "VE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Venezuela, Bolivarian Republic Of<\/span>"
            }
        },
        "VN": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Viet Nam<\/span>"
            }
        },
        "UA": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Ukraine<\/span>"
            }
        },
        "UY": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Uruguay<\/span>"
            }
        },
        "YE": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Yemen<\/span>"
            }
        },
        "ZM": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Zambia<\/span>"
            }
        },
        "ZW": {
            "value": "0",
            "href": "#",
            "tooltip": {
                "content": "<span style=\"font-weight:bold;\">Zimbabwe<\/span>"
            }
        }*/
    }
});
