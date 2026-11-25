import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logarithmic oscillatory component
        log_osc = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.8 * np.log(1.0 + np.abs(x[i]))
            amp = 1.5 + 0.5 * np.sin(0.5 * x[i])
            log_osc += amp * np.sin(freq * x[i] + 0.3 * np.cos(2.0 * x[i]))
        
        # Dynamic elliptic valley structure
        ellipse_valley = 0.0
        for i in range(self.dim):
            a = 1.0 + 0.6 * np.cos(0.4 * x[i])
            b = 1.0 + 0.4 * np.sin(0.3 * x[i])
            ellipse_valley += (x[i] - a * np.sin(0.5 * x[i]))**2 / a + (x[i] - b * np.cos(0.6 * x[i]))**2 / b
        
        # Multi-peak trigonometric structure with dynamic phase shifts
        trig_peaks = 0.0
        for i in range(self.dim):
            for j in range(3):
                phase_shift = 0.5 * np.sin(0.7 * x[i] + j)
                amplitude = 1.2 + 0.8 * np.cos(0.4 * x[i])
                trig_peaks += amplitude * np.cos(2.0 * x[i] + phase_shift) * np.exp(-0.5 * (x[i] - j)**2)
        
        # Cross-dimensional trigonometric coupling with varying interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                interaction = 0.8 + 0.4 * np.sin(0.3 * x[i]) * np.cos(0.5 * x[j])
                coupling += interaction * np.sin(0.7 * (x[i] + x[j])) * np.cos(0.4 * (x[i] - x[j]))
        
        # Saddle-point with dynamic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.7 + 0.3 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # High-frequency chaotic component with dynamic amplitude
        chaos = 0.0
        for i in range(self.dim):
            amp = 0.5 + 0.3 * np.sin(1.2 * x[i])
            chaos += amp * np.sin(8.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Dimensionally adaptive normalization
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return (0.22 * log_osc + 0.25 * ellipse_valley + 0.23 * trig_peaks + 
                0.15 * coupling + 0.10 * saddle + 0.05 * chaos) * dim_factor