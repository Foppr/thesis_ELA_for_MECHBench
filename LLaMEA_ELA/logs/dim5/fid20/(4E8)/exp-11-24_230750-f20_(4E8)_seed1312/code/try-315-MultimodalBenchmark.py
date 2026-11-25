import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillatory component with modified modulation
        chaotic_osc = 0.0
        for i in range(self.dim):
            freq_mod = 1.5 + 0.5 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i])
            amp_mod = 1.2 + 0.3 * np.sin(0.4 * x[i]**2)
            chaotic_osc += amp_mod * np.sin(freq_mod * x[i] + 0.6 * np.sin(1.8 * x[i]))
        
        # Adaptive fractal landscape with altered scale factors
        fractal = 0.0
        for i in range(self.dim):
            scale_factor = 1.3 + 0.6 * np.sin(0.4 * x[i]) * np.cos(0.2 * x[i])
            fractal += scale_factor * (np.sin(2.5 * x[i]) + 0.4 * np.cos(1.8 * x[i]))
        
        # Multi-peak Gaussian with adjusted center, variance, and amplitude
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -3.5 + 2.5 * j
                variance = 1.2 + 0.3 * np.sin(0.6 * x[i])
                amplitude = 1.3 + 0.5 * np.cos(0.3 * x[i]) * np.sin(0.5 * x[i]**2)
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional polynomial coupling with modified interaction coefficients
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coeff = 0.9 + 0.3 * np.sin(0.4 * x[i]) * np.cos(0.1 * x[j])
                coupling += coeff * (x[i]**2.5 + x[j]**2.5) * np.sin(0.3 * (x[i] - x[j]))
        
        # Saddle-point structure with modified chaotic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.8 + 0.2 * np.sin(0.8 * x[i]) * np.cos(0.5 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Additional chaotic component with modified frequency
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.3 * np.sin(3.5 * x[i]) * np.cos(2.5 * x[i]) * np.sin(0.6 * x[i]**2)
        
        # Dimensionally adaptive weighting and normalization
        dim_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        return (0.21 * chaotic_osc + 0.22 * fractal + 0.25 * gaussian_peaks + 
                0.19 * coupling + 0.11 * saddle + 0.06 * chaos) * dim_factor