import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic logarithmic oscillatory component with multiple frequencies
        log_osc = 0.0
        for i in range(self.dim):
            freq1 = 2.1 + 1.8 * np.log(1.0 + np.abs(x[i]))
            freq2 = 1.1 + 0.9 * np.sin(0.7 * x[i])
            amp1 = 2.5 + 1.5 * np.sin(0.5 * x[i])
            amp2 = 1.6 + 1.1 * np.cos(0.3 * x[i])
            log_osc += amp1 * np.sin(freq1 * x[i] + 0.3 * np.cos(2.0 * x[i])) + \
                      amp2 * np.cos(freq2 * x[i] + 0.4 * np.sin(1.5 * x[i]))
        
        # Dynamic elliptic valley structure with asymmetric parameters
        ellipse_valley = 0.0
        for i in range(self.dim):
            a = 2.0 + 1.1 * np.cos(0.4 * x[i])
            b = 1.1 + 0.9 * np.sin(0.3 * x[i])
            c = 1.6 + 0.7 * np.tan(0.2 * x[i])
            ellipse_valley += ((x[i] - a * np.sin(0.5 * x[i]))**2 / a + 
                              (x[i] - b * np.cos(0.6 * x[i]))**2 / b + 
                              (x[i] - c * np.exp(-0.1 * x[i]))**2 / c)
        
        # Multi-peak trigonometric structure with dynamic phase shifts and Gaussian modulations
        trig_peaks = 0.0
        for i in range(self.dim):
            for j in range(4):
                phase_shift = 0.8 * np.sin(0.9 * x[i] + j)
                amplitude = 2.0 + 1.5 * np.cos(0.5 * x[i])
                gaussian_mod = np.exp(-0.4 * (x[i] - j)**2)
                trig_peaks += amplitude * np.cos(3.0 * x[i] + phase_shift) * gaussian_mod
        
        # Cross-dimensional trigonometric coupling with polynomial interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                poly_interaction = 1.5 + 0.8 * (x[i]**3 + x[j]**3)  # Changed to cubic
                coupling += poly_interaction * np.sin(0.9 * (x[i] + x[j])) * np.cos(0.7 * (x[i] - x[j]))
        
        # Saddle-point with enhanced dynamic modulation and multiple interactions
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                modulator1 = 1.1 + 0.6 * np.sin(0.7 * x[i]) * np.cos(0.6 * x[i+1])
                modulator2 = 0.9 + 0.5 * np.cos(0.5 * x[i+2]) * np.sin(0.8 * x[i])
                saddle += (x[i]**2 - x[i+1]**2) * modulator1 + (x[i+1]**2 - x[i+2]**2) * modulator2
        
        # High-frequency chaotic component with dynamic amplitude and multiple harmonics
        chaos = 0.0
        for i in range(self.dim):
            amp1 = 1.1 + 0.7 * np.sin(1.5 * x[i])
            amp2 = 0.9 + 0.6 * np.cos(2.0 * x[i])
            chaos += (amp1 * np.sin(12.0 * x[i]) * np.cos(5.0 * x[i]) * 
                     np.exp(-0.2 * x[i]**2) + amp2 * np.cos(10.0 * x[i]) * np.sin(4.0 * x[i]))
        
        # Additional Gaussian peak structure for increased multimodality
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(5):
                peak_height = 3.0 + 2.5 * np.sin(0.4 * x[i])  # Increased height
                gaussian_peaks += peak_height * np.exp(-0.6 * (x[i] - j)**2)
        
        # Dimensionally adaptive normalization
        dim_factor = 1.5 + 0.5 * np.log(self.dim + 1)
        return (0.21 * log_osc + 0.23 * ellipse_valley + 0.25 * trig_peaks + 
                0.18 * coupling + 0.15 * saddle + 0.08 * chaos + 0.05 * gaussian_peaks) * dim_factor