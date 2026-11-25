import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested chaotic oscillatory component with multi-frequency modulation and cubic harmonics
        chaotic_osc = 0.0
        for i in range(self.dim):
            freq_mod = 2.0 + 1.5 * np.sin(0.9 * x[i]) * np.cos(0.7 * x[i])
            amp_mod = 1.5 + 1.0 * np.sin(0.5 * x[i]**2) * np.cos(0.4 * x[i])
            chaotic_osc += amp_mod * np.sin(freq_mod * x[i] + 0.8 * np.sin(3.0 * x[i]) + 0.5 * np.sin(5.0 * x[i]) + 0.2 * np.sin(7.0 * x[i]))
        
        # Dynamic fractal landscape with recursive sine-wave modulation and polynomial scaling
        fractal = 0.0
        for i in range(self.dim):
            scale_factor = 1.5 + 1.1 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i])
            fractal += scale_factor * (np.sin(5.0 * x[i]) + 0.7 * np.cos(4.0 * x[i]) + 0.5 * np.sin(3.0 * x[i]) + 0.3 * np.cos(2.0 * x[i]))
        
        # Multi-peak Gaussian with time-varying centers, dynamic variances, amplitude modulation, and cross-dimensional coupling
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(7):
                center = -4.0 + 1.5 * j + 0.6 * np.sin(0.9 * x[i])
                variance = 1.5 + 0.8 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i]**2)
                amplitude = 2.5 + 1.0 * np.cos(0.6 * x[i]) * np.sin(0.8 * x[i]**3)
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2) * (1.0 + 0.3 * np.sin(0.5 * x[i]))
        
        # Cross-dimensional polynomial coupling with adaptive interaction coefficients and higher-order terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coeff = 1.2 + 0.8 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[j]) * np.sin(0.3 * x[i]**2)
                coupling += coeff * (x[i]**5 + x[j]**5 + x[i]**3 * x[j]**2) * np.sin(0.6 * (x[i] - x[j]))
        
        # Saddle-point structure with dynamic modulation, dimensionally adaptive interaction, and chaotic perturbations
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.9 + 0.5 * np.sin(1.2 * x[i]) * np.cos(0.8 * x[i+1]) * np.sin(0.6 * x[i]**2)
                saddle += (x[i]**4 - x[i+1]**4) * modulator + 0.2 * np.sin(5.0 * x[i] + 3.0 * x[i+1])
        
        # Enhanced chaotic component with higher frequency oscillations, cubic modulation, and exponential scaling
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.7 * np.sin(6.0 * x[i]) * np.cos(5.0 * x[i]) * np.sin(0.9 * x[i]**3) + 0.4 * np.cos(7.0 * x[i]) + 0.1 * np.sin(8.0 * x[i])
        
        # Dimensionally adaptive weighting with exponential scaling factor and nonlinearity
        dim_factor = 1.2 + 0.5 * np.log(self.dim + 3) + 0.2 * np.sin(0.3 * self.dim)
        return (0.30 * chaotic_osc + 0.25 * fractal + 0.22 * gaussian_peaks + 
                0.18 * coupling + 0.08 * saddle + 0.07 * chaos) * dim_factor