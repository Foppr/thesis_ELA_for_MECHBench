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
            freq_mod = 1.5 + 1.2 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i])
            amp_mod = 1.2 + 0.8 * np.sin(0.4 * x[i]**2)
            chaotic_osc += amp_mod * np.sin(freq_mod * x[i] + 0.6 * np.sin(2.5 * x[i]))
        
        # Adaptive fractal landscape with multi-scale recursive structure
        fractal = 0.0
        for i in range(self.dim):
            scale_factor = 1.3 + 0.9 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            fractal += scale_factor * (np.sin(4.0 * x[i]) + 0.7 * np.cos(2.5 * x[i]))
        
        # Multi-peak Gaussian with dynamic center, variance, and amplitude
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(4):
                center = -4.5 + 2.5 * j
                variance = 1.3 + 0.6 * np.sin(0.6 * x[i])
                amplitude = 2.0 + 0.8 * np.cos(0.5 * x[i]) * np.sin(0.7 * x[i]**2)
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional polynomial coupling with dynamic interaction coefficients
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coeff = 1.0 + 0.6 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[j])
                coupling += coeff * (x[i]**4 + x[j]**4) * np.sin(0.5 * (x[i] - x[j]))
        
        # Saddle-point structure with enhanced chaotic modulation and dimensionality adaptation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.8 + 0.4 * np.sin(1.0 * x[i]) * np.cos(0.7 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Additional chaotic component with higher frequency oscillations
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.6 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i]) * np.sin(0.8 * x[i]**2)
        
        # Hyper-chaotic component with cubic modulation and exponential scaling
        hyperchaos = 0.0
        for i in range(self.dim):
            hyperchaos += 0.3 * np.sin(6.0 * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Dimensionally adaptive weighting and normalization
        dim_factor = 1.2 + 0.3 * np.log(self.dim + 1)
        return (0.25 * chaotic_osc + 0.25 * fractal + 0.20 * gaussian_peaks + 
                0.15 * coupling + 0.10 * saddle + 0.05 * chaos + 0.03 * hyperchaos) * dim_factor