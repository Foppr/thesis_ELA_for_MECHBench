import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulation with non-linear frequency coupling
        wave_mod = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i + x[i % self.dim])
            amp = 1.0 + 0.4 * np.cos(0.5 * i + x[(i+1) % self.dim])
            wave_mod += amp * np.sin(freq * x[i] + 0.1 * np.sum(x[:i])) * np.tanh(0.5 * x[i])
        
        # Dynamic Gaussian potentials with time-varying weights and positions
        pot_energy = 0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.4 * i + np.sum(x) / self.dim)
            weight = 1.0 + 0.5 * np.cos(0.6 * i + x[i])
            pot_energy += weight * np.exp(-0.3 * (x[i] - center)**2) * (1.0 + 0.3 * np.sin(4.0 * x[i]))
        
        # Radial distortion with fractal-like behavior and multiple interference patterns
        radial_sym = 0
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            radial_sym = (np.sin(7.0 * r) + 0.5 * np.cos(11.0 * r)) * np.exp(-0.15 * r) + \
                         0.4 * np.sin(3.0 * r + 0.2 * np.sum(x)) * np.cos(2.0 * r)
        
        # Cross-dimensional coupling with hyperbolic interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                cross_coupling += 0.3 * diff**2 * np.tanh(0.1 * (x[i]**2 + x[j]**2))
        
        # Novel chaotic noise component with memory effects
        noise = 0
        for i in range(self.dim):
            noise += 0.2 * np.sin(9.0 * x[i] + 0.3 * np.sum(x[:i])) * np.cos(5.0 * x[i] + 0.4 * np.sum(x[i:]))
        
        # Combine all components with dynamic scaling factors
        return 1.8 * pot_energy + 1.5 * wave_mod + 1.0 * radial_sym + 0.7 * cross_coupling + 0.4 * noise + 3.0 * self.dim