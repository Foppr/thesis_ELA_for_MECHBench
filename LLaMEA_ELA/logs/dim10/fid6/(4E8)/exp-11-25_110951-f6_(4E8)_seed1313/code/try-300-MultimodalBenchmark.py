import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with adaptive basis functions
        r_squared = np.sum(x_norm**2)
        radial = 0.0
        for i in range(self.dim):
            # Adaptive radial basis with varying widths and amplitudes
            width = 1.0 + 0.5 * np.sin(3.0 * x_norm[i])
            amplitude = 1.0 + 0.7 * np.cos(4.0 * x_norm[i])
            radial += amplitude * np.exp(-0.5 * (x_norm[i]**2) / width**2)
        
        # Chaotic gradient coupling with fractal-like behavior
        gradient_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling based on distance and angle with fractal scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                angle = np.arctan2(x_norm[j], x_norm[i])
                coupling_factor = 1.0 + 0.6 * np.sin(7 * angle) * np.cos(4 * dist) * np.sin(2 * np.pi * dist)
                gradient_coupling += coupling_factor * (x_norm[i]**2 + x_norm[j]**2) * np.exp(-dist**2)
        
        # Logarithmic barrier potentials with stochastic basin attraction
        basin_attraction = 0.0
        for i in range(self.dim):
            # Basin with logarithmic depth and stochastic perturbation
            base_depth = (x_norm[i]**2) * (1.0 + 0.4 * np.sin(8 * x_norm[i]))
            stochastic_perturb = 0.3 * np.random.normal(0, 1) * np.cos(5 * x_norm[i])
            basin_attraction += base_depth + stochastic_perturb
        
        # Spectral harmonic interference with log-periodic oscillations
        harmonic = 0.0
        for i in range(self.dim):
            freq = 12 + 4 * np.sin(3.0 * x_norm[i])
            phase = 0.6 * np.cos(6.0 * x_norm[i])
            harmonic += np.sin(freq * x_norm[i] + phase) * np.cos(freq * x_norm[i] * 0.7) * np.log(1 + np.abs(x_norm[i]))
        
        # Combined result with global scaling and non-uniform curvature
        result = radial + 0.7 * gradient_coupling + 0.5 * basin_attraction + 0.4 * harmonic
        
        # Global scaling based on distance from origin with logarithmic modification
        global_scale = 1.0 + 0.6 * np.log(1 + 0.3 * r_squared)
        
        return global_scale * result