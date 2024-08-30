import React, { useState } from "react";
import{
    Typography,
    Stack,
    Chip,
    Paper,
    Grid,
    Container,
    Paper,
    Grid,
    TextField,
    Checkbox,
    FromGrop,
    FormControlLabel,
    Autocomplete,
    CircularProgress,
    Button,
} form "@mui/marerial";
import{ LocalizationProvider, TimePicker} from "@mui/lab";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { AddCircleOutlined } from "@mui/icons-material";
import Swal from "sweetalert2";
import axios from "axios";

const AddConstraints = () => {
    const [monday, setMonday] = useState(false);
    const [tuesday, setTuesday] = useState(false);4
    const [wednesday, setWednesday] = useState(false);
    const [thursday, setThursday] = useState(false);
    const [friday, setFriday] = useState(false);
    const [saturday, setSaturday] = useState(false);
    const [sunday, setSunday] = useState(false);
    const [startMondayHours, setStartMondayHours] = useState(new Date())
    const [endMondayHours, setEndMondayHours] = useState(new Date())
    const [startTuesdayHours, setStartTuesdayHours] = useState(new Date())
    const [endTuesdayHours, setEndTuesdayHours] = useState(new Date())
    const [startWednesdayHours, setStartWednesdayHours] = useState(new Date())
    const [endWednesdayHours, setEndWednesdayHours] = useState(new Date())
    const [startThursdayHours, setStartThursdayHours] = useState(new Date())
    const [endThursdayHours, setEndThursdayHours] = useState(new Date())
    const [startFridayHours, setStartFridayHours] = useState(new Date())
    const [endFridayHours, setEndFridayHours] = useState(new Date())
    const [startSaturdayHours, setStartSaturdayHours] = useState(new Date())
    const [endSaturdayHours, setEndSaturdayHours] = useState(new Date())
    const [startSundayHours, setStartSundayHours] = useState(new Date())
    const [endSundayHours, setEndSundayHours] = useState(new Date())
    const [checkedA, setCheckedA] = useState(false);
    //eslint-disable-next-line
    const [checkedB, setCheckedB] = useState(false);
    const[loading, setLoading] = useState(true);
    const[subjects, setSubjects] = useState([]);
    const[sub1, setSub1] = useState("");
    const[sub2, setSub2] = useState("");
    const[nsub1, setnSub1] = useState("");
    const[nsub2, setnSub2] = useState("");

    const handleMonday = (newValue) => {
        setStartMondayHours(newValue);
    };

    const handleTuesday = (newValue) => {
        setStartTuesdayHours(newValue);
    };

    const handleWednesday = (newValue) => {
        setStartWednesdayHours(newValue);
    };

    const handleThursday = (newValue) => {
        setStartThursdayHours(newValue);
    };

    const handleFriday = (newValue) => {
        setStartFridayHours(newValue);
    };

    const handleSaturday = (newValue) => {
        setStartSaturdayHours(newValue);
    };

    const handleSunday = (newValue) => {
        setStartSundayHours(newValue);
    };

    const handleMondayEnd = (newValue) => {
        setEndMondayHours(newValue);
    };

    const handleTuesdayEnd = (newValue) => {
        setEndTuesdayHours(newValue);
    };  

    const handleWednesdayEnd = (newValue) => {
        setEndWednesdayHours(newValue);
    };

    const handleThursdayEnd = (newValue) => {
        setEndThursdayHours(newValue);
    };

    const handleFridayEnd = (newValue) => {
        setEndFridayHours(newValue);
    };

    const handleSaturdayEnd = (newValue) => {
        setEndSaturdayHours(newValue);
    };

    const handleSundayEnd = (newValue) => {
        setEndSundayHours(newValue);
    };

    const handleSubmit = () => {
        var working_days = [];
        if(monday) working_days.push({
            day: "Monday",
            start_hr: startMondayHours.getHours(),
            end_hr: endMondayHours.getHours()
            total_hours: 
                parseInt(endMondayHours.getHours()) - 
                parseInt(startMondayHours.getHours())
        });
    }
    if(tuesday){
        working_days.push({
            day: "Tuesday",
            start_hr: startTuesdayHours.getHours(),
            end_hr: endTuesdayHours.getHours(),
            total_hours: 
                parseInt(endTuesdayHours.getHours()) - 
                parseInt(startTuesdayHours.getHours())
        });
    }
    if(wednesday){
        working_days.push({
            day: "Wednesday",
            start_hr: startWednesdayHours.getHours(),
            end_hr: endWednesdayHours.getHours(),
            total_hours: 
                parseInt(endWednesdayHours.getHours()) - 
                parseInt(startWednesdayHours.getHours())
        });
    }
    if(thursday){
        working_days.push({
            day: "Thursday",
            start_hr: startThursdayHours.getHours(),
            end_hr: endThursdayHours.getHours(),
            total_hours: 
                parseInt(endThursdayHours.getHours()) - 
                parseInt(startThursdayHours.getHours())
        });
    }
    if(friday){
        working_days.push({
            day: "Friday",
            start_hr: startFridayHours.getHours(),
            end_hr: endFridayHours.getHours(),
            total_hours: 
                parseInt(endFridayHours.getHours()) - 
                parseInt(startFridayHours.getHours())
        });
    }
    if(saturday){
        working_days.push({
            day: "Saturday",
            start_hr: startSaturdayHours.getHours(),
            end_hr: endSaturdayHours.getHours(),
            total_hours: 
                parseInt(endSaturdayHours.getHours()) - 
                parseInt(startSaturdayHours.getHours())
        });
    }
    if(sunday){
        working_days.push({
            day: "Sunday",
            start_hr: startSundayHours.getHours(),
            end_hr: endSundayHours.getHours(),
            total_hours: 
                parseInt(endSundayHours.getHours()) - 
                parseInt(startSundayHours.getHours())
        });
    }

    var consecutive_subjects = [sub1, sub2];
    var non_consecutive_subjects = [nsub1, nsub2];
    var body = {
        working_days: working_days,
        consecutive_subjects: consecutive_subjects,
        non_consecutive_subjects: non_consecutive_subjects
    };
    console.log(body);
    axios
        .post("http://localhost:8000/add.constraints", body)
        .then(() => {
            Swal.fire({
                text: "Constraints added successfully!",
                icon: "Success"
            });
            setMonday(false);
            setTuesday(false);
            setWednesday(false);
            setThursday(false);
            setFriday(false);
            setSaturday(false);
            setSunday(false);
            setStartMondayHours(new Date());
            setEndMondayHours(new Date());
            setStartTuesdayHours(new Date());
            setEndTuesdayHours(new Date());
            setStartWednesdayHours(new Date());
            setEndWednesdayHours(new Date());
            setStartThursdayHours(new Date());
            setEndThursdayHours(new Date());
            setStartFridayHours(new Date());
            setEndFridayHours(new Date());
            setStartSaturdayHours(new Date());
            setEndSaturdayHours(new Date());
            setStartSundayHours(new Date());
            setEndSundayHours(new Date());
            setCheckedA(false);
            setCheckedB(false);
            setSub1("");
            setSub2("");
            setnSub1("");
            setnSub2("");

        })
        .catch((e) => console.log(e));
    };

    useEffect(() => {
        axios.get("http://localhost:8000/get-courses").then((res) => {
        setLoading(false);
        var temp_subjects = [];
          // eslint-disable-next-line
        res.data.map((item) => {
            temp_subjects.push({ label: item.name, value: item.name });
        });
        setSubjects(temp_subjects);
        });
    }, []);
    return(
        <>
        {loading ?(
            <CircularProgress/>
        ) : (
            <>
            <container component="main" maxWitdh="md" sx {{mb: 4}} >
                <Paper
                varient="outlined"
                sx{{my: {xs:3, md: 6}, p:{xs:2, md: 3} }}>
                >
                    <center>
                        <Typography varient="h6" gutterBottom>
                            Time Table Details
                        </Typography>
                    <center/>

                    <Grid container spacing={3}>
                        <Grid item xs={12} sm={3}>
                            <Stack direction="row" spacing={1} justifyContent="center">
                                {monday ? (
                                    <Chip
                                    lable="Monday"
                                    color="primary"
                                    omClick={() => setMonday(!monday)}
                                    />
                                ) : (
                                    
                                )}
                        </Grid>
                    </Grid>
                </>
        )}
        </>
    )
