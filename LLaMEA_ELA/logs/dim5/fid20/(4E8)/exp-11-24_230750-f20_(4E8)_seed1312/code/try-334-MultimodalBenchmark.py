import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic logarithmic oscillatory component with dynamic frequency modulation
        log_osc = 0.0
        for i in range(self.dim):
            freq = 1.5 + 1.2 * np.log(1.0 + np.abs(x[i])) * np.sin(0.3 * x[i])
            amp = 2.0 + 0.8 * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i])
            log_osc += amp * np.sin(freq * x[i] + 0.4 * np.cos(3.0 * x[i]))
        
        # Dynamic elliptic valley structure with asymmetric parameters
        ellipse_valley = 0.0
        for i in range(self.dim):
            a = 1.2 + 0.7 * np.cos(0.5 * x[i]) * np.sin(0.3 * x[i])
            b = 0.8 + 0.6 * np.sin(0.4 * x[i]) * np.cos(0.2 * x[i])
            ellipse_valley += (x[i] - a * np.sin(0.6 * x[i]))**2 / a + (x[i] - b * np.cos(0.7 * x[i]))**2 / b
        
        # Multi-peak trigonometric structure with dynamic phase shifts and amplitude variations
        trig_peaks = 0.0
        for i in range(self.dim):
            for j in range(4):
                phase_shift = 0.6 * np.sin(0.8 * x[i] + j * 0.5)
                amplitude = 1.5 + 1.0 * np.cos(0.5 * x[i]) * np.sin(0.3 * x[i])
                trig_peaks += amplitude * np.cos(2.5 * x[i] + phase_shift) * np.exp(-0.3 * (x[i] - j)**2)
        
        # Cross-dimensional trigonometric coupling with variable interaction strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                interaction = 1.0 + 0.5 * np.sin(0.4 * x[i]) * np.cos(0.6 * x[j]) * np.tan(0.2 * (x[i] + x[j]))
                coupling += interaction * np.sin(0.8 * (x[i] + x[j])) * np.cos(0.5 * (x[i] - x[j]))
        
        # Saddle-point with dynamic modulation and nonlinear interaction
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.8 + 0.4 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i+1]) * np.exp(-0.2 * (x[i] - x[i+1])**2)
                saddle += (x[i]**3 - x[i+1]**3) * modulator
        
        # High-frequency chaotic component with dynamic amplitude and phase
        chaos = 0.0
        for i in range(self.dim):
            amp = 0.8 + 0.5 * np.sin(1.5 * x[i]) * np.cos(0.8 * x[i])
            phase = 0.3 * np.sin(2.0 * x[i])
            chaos += amp * np.sin(9.0 * x[i] + phase) * np.cos(4.0 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Add novel adaptive conditioning with dimension-dependent scaling
        dim_factor = 1.5 + 0.3 * np.log(self.dim + 1) + 0.2 * np.sin(0.5 * self.dim)
        return (0.25 * log_osc + 0.28 * ellipse_valley + 0.25 * trig_peaks + 
                0.12 * coupling + 0.08 * saddle + 0.02 * chaos) * dim_factor