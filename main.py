import first as f
import time


if __name__ == '__main__':

    for i in range(8):
        link = 'https://www.expedia.com'
        f.browser.get(link)
        time.sleep(5)

        # Choose flight tab
        choose_flight_only = f.browser.find_element_by_xpath("//button[@id='tab-flight-tab-hp']")
        choose_flight_only.click()

        f.ticket_type_chooser(f.return_ticket)

        f.departure_country_chooser('Munich')
        f.arrival_country_chooser('Denpasar')

        f.dep_date_choose('12', '27', '2019')
        f.return_date_chooser('01', '10', '2020')

        f.search()

        f.compile_data()

        current_values = f.df.iloc[0]

        cheapest_dep_time = current_values[0]
        cheapest_arr_time = current_values[1]
        cheapest_airline = current_values[2]
        cheapest_duration = current_values[3]
        cheapest_stops = current_values[4]
        cheapest_price = current_values[-1]

        print('run {} completed'.format(i))


        # TODO: Implement Telegram Interface

        # Create message template for email
        def create_msg():
            global msg
            msg = '\nCurrent Cheapest flight:\n\nDeparture time: {}\nArrival time: {}\nAirline: {}\nFlight duration: {}\nNo. of stops: {}\nPrice: {}\n'.format(
                cheapest_dep_time,
                cheapest_arr_time,
                cheapest_airline,
                cheapest_duration,
                cheapest_stops,
                cheapest_price)
            print(msg)


        create_msg()

        f.df.to_excel('Flight_Prices.xlsx', index=False)
        time.sleep(3600)