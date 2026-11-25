import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced radial basis function component with dynamic centers and widths
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.8) * 0.6 + 0.1 * np.cos(i * 0.3)
            width = 0.25 + 0.25 * np.sin(i * 0.5)
            rbf += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2) * (1.0 + 0.3 * np.sin(i * 0.7))
        
        # Enhanced sinusoidal oscillations with dynamic frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.2 + 0.3 * np.sin(i * 0.4))
            amp = 1.2 / (1.0 + 0.3 * i + 0.1 * np.cos(i * 0.6))
            sinusoidal += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Asymmetric cross-terms with dynamic coupling strengths and phase shifts
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asymmetry = (i + 1) / (j + 1)
                coupling = 0.6 * (asymmetry + 1.0 / asymmetry) * (1.0 + 0.2 * np.sin(i * 0.5))
                phase_shift = 0.3 * np.cos(i * j * 0.2)
                term = np.sin(coupling * x_scaled[i] * x_scaled[j] + phase_shift) * np.cos(coupling * x_scaled[i] * x_scaled[j] + phase_shift)
                cross_terms += term * (i + j + 1) * 0.15
        
        # Enhanced polynomial with mixed even and odd powers and dynamic coefficients
        polynomial = 0.0
        for i in range(self.dim):
            coeff = 0.3 + 0.1 * np.sin(i * 0.6)
            polynomial += coeff * (x_scaled[i]**2 + 0.5 * x_scaled[i]**3 + 0.2 * x_scaled[i]**4)
        
        # Distance-based conditioning with exponential scaling
        dist = np.sqrt(np.sum(x_scaled**2))
        conditioning = 0.7 * (self.dim - 1) * np.exp(dist**2 / (self.dim * 2.0))
        
        # Enhanced cubic interactions with dynamic phase shifts and variable coupling
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.4 * (i - j)) + 0.2 * np.cos(i * j * 0.3)
                coupling = 0.5 + 0.3 * np.sin(i * 0.7)
                cubic_interaction += (x_scaled[i]**3) * (x_scaled[j]**2) * np.cos(phase) * coupling
        
        # Additional trigonometric coupling with higher frequency components
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = (i + j + 1) * np.pi * (1.0 + 0.2 * np.sin(i * 0.3))
                term = np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[j])
                trig_coupling += term * (i + j + 1) * 0.05
        
        # Combine all components with carefully tuned weights
        return 2.2 * rbf + 2.0 * sinusoidal + 1.8 * cross_terms + 1.0 * polynomial + conditioning + 0.9 * cubic_interaction + 0.8 * trig_coupling