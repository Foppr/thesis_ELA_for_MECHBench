import numpy as np

class FractalEllipticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar fractal pattern with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0
            term = 0.0
            for k in range(1, 8):
                scale *= 0.5
                term += scale * np.sin(k * x[i]) * np.cos(k * x[i])
            fractal += term ** 2
        
        # Adaptive elliptic conditioning with dynamic eccentricity
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            elliptic += eccentricity * (x[i] ** 2) + 0.1 * (x[i] ** 4)
        
        # Dynamic harmonic interference with frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(0.7 * x[i])
            harmonic += freq_mod * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i])
        
        # Multi-scale oscillatory components with varying amplitudes
        oscillatory = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.4 * x[i])
            freq = 2.0 + 0.8 * np.cos(0.6 * x[i])
            oscillatory += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric basin with piecewise polynomial and exponential components
        asymmetric = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asymmetric += 0.3 * x[i]**3 + 0.2 * np.exp(-x[i])
            else:
                asymmetric += 0.4 * x[i]**2 + 0.1 * np.exp(x[i])
        
        # Cross-dimensional coupling with dynamic phase relationships
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.3 * (x[i] + x[j])) * np.cos(0.2 * (x[i] - x[j]))
                weight = 1.0 + 0.2 * np.sin(x[i]) * np.cos(x[j])
                coupling += weight * phase * np.exp(-0.05 * ((x[i] - x[j])**2))
        
        # Combined fitness with weighted components
        total = 0.3 * fractal + 0.25 * elliptic + 0.2 * harmonic + 0.15 * oscillatory + 0.08 * asymmetric + 0.02 * coupling
        
        return total