import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic tangent oscillatory component with chaotic modulation
        tanh_osc = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
            tanh_osc += np.tanh(freq * x[i]) * np.sin(3.0 * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Multi-scale Gaussian mixture with adaptive variances and cross-dimensional couplings
        gaussian_mixture = 0.0
        for i in range(self.dim):
            centers = np.linspace(-4, 4, 7)
            for j in range(7):
                center = centers[j]
                variance = 0.3 + 0.4 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
                gaussian_mixture += 0.15 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Dynamic saddle-point structure with asymmetric coupling and time-varying coefficients
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                asymmetry = 1.0 + 0.3 * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i+1])
                saddle += (x[i]**2 - asymmetry * x[i+1]**2) * np.cos(0.4 * x[i]) * np.sin(0.6 * x[i+1])
        
        # Fractional Brownian motion inspired fractal component with logarithmic spiral modulation
        fbm = 0.0
        for i in range(self.dim):
            spiral_factor = 1.0 + 0.2 * np.sin(np.log(abs(x[i]) + 1))
            fbm += np.sin(x[i]) * np.cos(0.8 * x[i]) * np.exp(-0.15 * abs(x[i])) * spiral_factor
        
        # Cross-dimensional coupling with quantum-like potential interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quantum_phase = np.sin(0.2 * (x[i] + x[j]))
                coupling += (x[i] * x[j])**3 * quantum_phase * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Resonance peak structure with adaptive amplitude modulation
        resonance = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.5 * np.cos(0.9 * x[i]) * np.sin(0.4 * x[i])
            resonance += amp_mod * np.sin(2.5 * x[i]) * np.cos(1.2 * x[i]) * np.exp(-0.08 * abs(x[i]))
        
        # Combined function with dimensionally adaptive weighting and noise suppression
        dim_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        noise_suppression = 1.0 / (1.0 + 0.02 * np.sum(x**2))
        return (0.25 * tanh_osc + 0.3 * gaussian_mixture + 0.15 * saddle + 
                0.12 * fbm + 0.1 * coupling + 0.08 * resonance) * dim_factor * noise_suppression