import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks
        radial = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i]
            radial += np.exp(-0.5 * ((x - center) / (1.0 + 0.1 * i))**2) * (1.0 + 0.3 * np.sin(i))
        
        # Sinusoidal oscillation component
        sin_component = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * i)
            amp = 1.0 + 0.2 * np.cos(0.4 * i)
            sin_component += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric conditioning component
        asym = 0
        for i in range(self.dim):
            if x[i] >= 0:
                asym += (x[i]**3) * np.exp(-0.2 * x[i])
            else:
                asym += (x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interaction with varying strength
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Polynomial modulation with dynamic exponents
        poly_mod = 0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.4 * np.sin(0.5 * i)
            poly_mod += (x[i]**exp_factor) * np.exp(-0.1 * abs(x[i]))
        
        # Add a new component: hybrid Gaussian-sigmoidal with dynamic scaling
        gaussian_sigmoid = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.cos(0.4 * i)
            gaussian_sigmoid += (np.exp(-0.5 * (x[i] / scale)**2) * 
                               (1.0 / (1.0 + np.exp(-x[i]))))
        
        # Combine all components
        return (radial * 0.6 +
                sin_component * 0.4 +
                asym * 0.35 +
                interaction * 0.25 +
                poly_mod * 0.3 +
                gaussian_sigmoid * 0.2)