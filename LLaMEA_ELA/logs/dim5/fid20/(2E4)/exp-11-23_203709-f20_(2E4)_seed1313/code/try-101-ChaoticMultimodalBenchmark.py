import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced elliptic component with chaotic orientation and dynamic scaling
        elliptic = 0
        for i in range(self.dim):
            a = 1.0 + 0.4 * np.sin(1.1 * i + 0.5)
            b = 1.0 + 0.4 * np.cos(1.1 * i + 0.5)
            theta = 0.2 * i + 0.1 * np.sin(0.7 * i)
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            x_rot = cos_theta * x[i] - sin_theta * x[(i+1) % self.dim]
            y_rot = sin_theta * x[i] + cos_theta * x[(i+1) % self.dim]
            elliptic += (x_rot**2 / a**2 + y_rot**2 / b**2) * np.exp(-0.1 * (x[i]**2 + x[(i+1) % self.dim]**2))
        
        # Enhanced trigonometric coupling with chaotic phase modulation
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                phase = 0.5 * np.sin(0.8 * i + 0.3 * j)
                trig_coupling += np.sin(5.0 * dx + phase) * np.cos(2.0 * dx + phase) * (1.0 + 0.3 * np.abs(dx))
        
        # Stochastic perturbation with chaotic amplitude and frequency modulation
        stochastic = 0
        for i in range(self.dim):
            amp = 0.7 + 0.3 * np.sin(2.0 * i + 1.5)
            freq = 1.2 + 0.8 * np.cos(0.9 * i)
            stochastic += amp * np.random.normal(0, 1) * np.exp(-0.05 * x[i]**2) * np.sin(freq * x[i])
        
        # Polynomial landscape with chaotic degree modulation and dynamic bias
        poly = 0
        for i in range(self.dim):
            deg = 3 + int(4 * np.sin(0.7 * i + 0.8))
            bias = -2.0 + 4.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            poly += (x[i] - bias)**deg
        
        # Cross-dimensional interference with chaotic coupling weights
        interference = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x[i] - x[j])
                    weight = 0.5 + 0.5 * np.sin(1.3 * i + 0.9 * j)
                    interference += weight * np.exp(-dist) * np.cos(3.0 * dist)
        
        # Dimensionality scaling with chaotic conditioning factor
        dim_scaling = np.sum(np.exp(0.3 * np.arange(self.dim))) / self.dim
        
        # Novel spectral component with chaotic frequency modulation and multi-harmonic coupling
        spectral = 0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.6 * i + 0.4)
            harmonic_sum = 0
            for h in range(1, 6):
                harmonic_sum += h * np.sin(h * freq_mod * x[i] + h * 0.3 * i)
            spectral += harmonic_sum**2
        
        # Combined landscape with novel chaotic weighting and additional cross-term interactions
        return 2.1 * elliptic + 2.0 * trig_coupling + 1.1 * stochastic + 0.8 * poly + 1.5 * interference + 18.0 * dim_scaling + 0.7 * spectral + 0.3 * np.sum(x**4) + 0.2 * np.sum(np.sin(x))