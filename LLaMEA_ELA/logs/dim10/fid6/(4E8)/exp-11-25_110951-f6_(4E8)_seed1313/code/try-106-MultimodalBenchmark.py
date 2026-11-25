import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal self-similar structure with recursive scaling
        fractal_scale = 1.0 + 0.5 * np.sin(self.dim * np.pi / 8.0)
        x_scaled = x_norm * fractal_scale
        
        # Dynamic phase modulation with time-varying coupling
        t = 0.3 + 0.7 * np.sin(0.5 * self.dim * np.pi / 10.0)
        phase_mod = 1.0 + 0.4 * np.cos(t * x_scaled)
        
        # Energy landscape with multiple interacting potentials
        potential_1 = np.sum(np.sin(phase_mod * x_scaled) ** 2)
        potential_2 = np.sum(np.cos(phase_mod * x_scaled) ** 2)
        potential_3 = np.sum(np.tan(0.5 * phase_mod * x_scaled) ** 2)
        
        # Coupling between dimensions with fractal scaling
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_strength = 0.1 * np.exp(-0.1 * i)
            coupling_term += coupling_strength * (
                np.sin(2 * np.pi * x_scaled[i]) * np.cos(2 * np.pi * x_scaled[i+1]) +
                np.cos(3 * np.pi * x_scaled[i]) * np.sin(3 * np.pi * x_scaled[i+1])
            )
        
        # Adaptive conditioning based on dimensionality and fractal properties
        condition_factor = 1.0 + 0.3 * (self.dim - 1) * np.abs(np.cos(t))
        
        # Basin structure with dynamic center and chaotic perturbation
        center_shift = 0.2 * np.sin(t * x_scaled)
        basin = np.exp(-0.5 * np.sum((x_scaled - center_shift)**2)) * \
                np.prod(np.sin(3 * np.pi * (x_scaled + 0.1)))
        
        # Combine all components with dynamic weighting
        return condition_factor * (potential_1 + potential_2 + potential_3 + coupling_term + basin)