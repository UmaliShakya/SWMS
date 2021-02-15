export const darkTheme = {
  palette: {
    primary: {
      main: "#90caf9",
    },
    type: "dark",
  },
};

export const lightTheme = {
  palette: {
    primary: {
      light: "#4dabf5",
      main: "#2196f3",
      dark: "#1769aa",
    },
    secondary: {
      light: "#dd33fa",
      main: "#d500f9",
      dark: "#9500ae",
      contrastText: "#fff",
    },
    background: {
      default: "#fcfcfe",
    },
  },
  shape: {
    borderRadius: 10,
  },
  overrides: {
    RaMenuItemLink: {
      root: {
        borderLeft: "3px solid #fff",
      },
      active: {
        borderLeft: "3px solid #4f3cc9",
      },
    },
    MuiPaper: {
      elevation1: {
        boxShadow: "none",
      },
      root: {
        border: "1px solid #e0e0e3",
        backgroundClip: "padding-box",
      },
    },
    MuiButton: {
      contained: {
        backgroundColor: "#fff",
        color: "#4f3cc9",
        boxShadow: "none",
      },
    },
    MuiAppBar: {
      colorSecondary: {
        color: "#ffffff",
        backgroundColor: "#00CFC1",
      },
    },
    MuiLinearProgress: {
      colorPrimary: {
        backgroundColor: "#f5f5f5",
      },
      barColorPrimary: {
        backgroundColor: "#d7d7d7",
      },
    },
    MuiFilledInput: {
      root: {
        backgroundColor: "rgba(0, 0, 0, 0.04)",
        "&$disabled": {
          backgroundColor: "rgba(0, 0, 0, 0.04)",
        },
      },
    },
  },
};
