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
            day: 
        })
    }
}