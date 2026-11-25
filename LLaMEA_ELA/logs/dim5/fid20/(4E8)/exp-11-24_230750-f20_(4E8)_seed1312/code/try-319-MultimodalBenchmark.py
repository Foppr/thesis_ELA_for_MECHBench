import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested chaotic oscillatory component with multi-frequency modulation
        chaotic_osc = 0.0
        for i in range(self.dim):
            freq_mod = 1.5 + 1.2 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i])
            amp_mod = 1.2 + 0.8 * np.sin(0.4 * x[i]**2) * np.cos(0.3 * x[i])
            chaotic_osc += amp_mod * np.sin(freq_mod * x[i] + 0.7 * np.sin(3.0 * x[i]) + 0.3 * np.sin(5.0 * x[i]))
        
        # Dynamic fractal landscape with recursive sine-wave modulation
        fractal = 0.0
        for i in range(self.dim):
            scale_factor = 1.3 + 0.9 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i])
            fractal += scale_factor * (np.sin(4.0 * x[i]) + 0.6 * np.cos(3.0 * x[i]) + 0.4 * np.sin(2.0 * x[i]))
        
        # Multi-peak Gaussian with time-varying centers, dynamic variances, and amplitude modulation
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(5):
                center = -4.5 + 2.0 * j + 0.5 * np.sin(0.8 * x[i])
                variance = 1.2 + 0.6 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i]**2)
                amplitude = 2.0 + 0.8 * np.cos(0.5 * x[i]) * np.sin(0.7 * x[i]**3)
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional polynomial coupling with adaptive interaction coefficients
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coeff = 1.0 + 0.6 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[j]) * np.sin(0.2 * x[i]**2)
                coupling += coeff * (x[i]**4 + x[j]**4) * np.sin(0.5 * (x[i] - x[j]))
        
        # Saddle-point structure with dynamic modulation and dimensionally adaptive interaction
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.8 + 0.4 * np.sin(1.0 * x[i]) * np.cos(0.7 * x[i+1]) * np.sin(0.5 * x[i]**2)
                saddle += (x[i]**3 - x[i+1]**3) * modulator
        
        # Enhanced chaotic component with higher frequency oscillations and cubic modulation
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.6 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i]) * np.sin(0.8 * x[i]**3) + 0.3 * np.cos(6.0 * x[i])
        
        # Dimensionally adaptive weighting with exponential scaling factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 2)
        return (0.25 * chaotic_osc + 0.25 * fractal + 0.20 * gaussian_peaks + 
                0.15 * coupling + 0.10 * saddle + 0.05 * chaos) * dim_factor