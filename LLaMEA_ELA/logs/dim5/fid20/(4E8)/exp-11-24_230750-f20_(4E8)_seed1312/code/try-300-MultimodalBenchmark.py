import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillatory component with quaternion-inspired modulation
        chaotic_osc = 0.0
        for i in range(self.dim):
            freq_mod = 1.2 + 0.8 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            amp_mod = 1.0 + 0.5 * np.sin(0.3 * x[i]**2)
            chaotic_osc += amp_mod * np.sin(freq_mod * x[i] + 0.5 * np.sin(2.0 * x[i]))
        
        # Adaptive fractal landscape with multi-scale recursive structure
        fractal = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.7 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            fractal += scale_factor * (np.sin(3.0 * x[i]) + 0.5 * np.cos(2.0 * x[i]))
        
        # Multi-peak Gaussian with dynamic center, variance, and amplitude
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -4.0 + 3.0 * j
                variance = 1.0 + 0.4 * np.sin(0.5 * x[i])
                amplitude = 1.5 + 0.6 * np.cos(0.4 * x[i]) * np.sin(0.6 * x[i]**2)
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional polynomial coupling with dynamic interaction coefficients
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coeff = 0.8 + 0.4 * np.sin(0.3 * x[i]) * np.cos(0.2 * x[j])
                coupling += coeff * (x[i]**3 + x[j]**3) * np.sin(0.4 * (x[i] - x[j]))
        
        # Saddle-point structure with enhanced chaotic modulation and dimensionality adaptation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.7 + 0.3 * np.sin(0.9 * x[i]) * np.cos(0.6 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Additional chaotic component with higher frequency oscillations
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.4 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * np.sin(0.7 * x[i]**2)
        
        # Dimensionally adaptive weighting and normalization
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return (0.22 * chaotic_osc + 0.23 * fractal + 0.24 * gaussian_peaks + 
                0.18 * coupling + 0.12 * saddle + 0.07 * chaos) * dim_factor