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
            width = 1.0 + 0.3 * np.sin(2.0 * x_norm[i])
            amplitude = 1.0 + 0.5 * np.cos(3.0 * x_norm[i])
            radial += amplitude * np.exp(-0.5 * (x_norm[i]**2) / width**2)
        
        # Dynamic gradient coupling with time-like parameter
        gradient_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling based on distance and angle
                dist = np.abs(x_norm[i] - x_norm[j])
                angle = np.arctan2(x_norm[j], x_norm[i])
                coupling_factor = 1.0 + 0.4 * np.sin(5 * angle) * np.cos(3 * dist)
                gradient_coupling += coupling_factor * (x_norm[i]**2 + x_norm[j]**2) * np.exp(-dist**2)
        
        # Probabilistic basin attraction with stochastic elements
        basin_attraction = 0.0
        for i in range(self.dim):
            # Basin with probabilistic depth and stochastic perturbation
            base_depth = (x_norm[i]**2) * (1.0 + 0.3 * np.sin(7 * x_norm[i]))
            stochastic_perturb = 0.2 * np.random.normal(0, 1) * np.cos(4 * x_norm[i])
            basin_attraction += base_depth + stochastic_perturb
        
        # High-frequency harmonic interference with dynamic phase
        harmonic = 0.0
        for i in range(self.dim):
            freq = 10 + 3 * np.sin(2.0 * x_norm[i])
            phase = 0.5 * np.cos(5.0 * x_norm[i])
            harmonic += np.sin(freq * x_norm[i] + phase) * np.cos(freq * x_norm[i] * 0.8)
        
        # Combined result with global scaling and non-uniform curvature
        result = radial + 0.6 * gradient_coupling + 0.4 * basin_attraction + 0.3 * harmonic
        
        # Global scaling based on distance from origin
        global_scale = 1.0 + 0.5 * np.exp(-0.2 * r_squared)
        
        return global_scale * result