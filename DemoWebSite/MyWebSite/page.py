from flask import Flask, render_template #imporing Flask object from flask librarly
#render_template fetch html file and store that file somewhere in our python application

app=Flask(__name__) #instantiate that class object,__name__ indicate current script is executing if any other script is there we have to write that script name

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN
    start_time=datetime.datetime(2010,1,1)
    end_time=datetime.datetime(2019,4,16)
    df=data.DataReader(name="TCS.NS",data_source="yahoo",start=start_time,end=end_time)

    def inc_dec(cl,op):
        if cl > op:
            value="Increase"
        elif cl < op:
            value="Decrease"
        else:
            value="Same"
        return value

    df["Status"]=[inc_dec(cl,op) for cl, op in zip(df.Close,df.Open)]



    df["Middle"]=(df.Close+df.Open)/2
    df["Height"]=abs(df.Close-df.Open)


    p=figure(x_axis_type="datetime",width=1000,height=300,sizing_mode="scale_width")
    p.title.text="Its A Sample Chart"
    p.grid.grid_line_alpha=0.6
    hours_12=12*60*60*1000

    p.segment(df.index,df.High,df.index,df.Low,color="black")
    p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],hours_12,
           df.Height[df.Status=="Increase"],fill_color="green",line_color="blue")
    p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],hours_12,
           df.Height[df.Status=="Decrease"],fill_color="red",line_color="blue")

    script1, div1=components(p)
    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]
    return render_template("Plot.html",script1=script1,
    div1=div1,cdn_js=cdn_js,cdn_css=cdn_css)

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/about/')
def about():
    return render_template("About.html")

@app.route('/button/')
def button():
    return render_template("button.html")


if __name__=="__main__":
    app.run(debug=True)
