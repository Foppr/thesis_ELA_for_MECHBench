import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = min(6, max(3, dim // 2))
        self.adaptivity_factor = 0.5 + 0.3 * (dim / 15.0)
        # Add quaternion-inspired rotational components
        self.quat_coeffs = np.random.uniform(0.5, 1.5, size=(4, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] for fractal generation
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal component using recursive self-similarity with quaternion modulation
        fractal_value = 0.0
        for i in range(self.fractal_depth):
            scale = 2 ** i
            period = 2 * np.pi / scale
            # Apply quaternion rotation to input dimensions
            rotated_x = np.zeros_like(x_norm)
            for d in range(self.dim):
                q = self.quat_coeffs[:, d]
                rotated_x[d] = x_norm[d] * q[0] + x_norm[(d+1)%self.dim] * q[1] - x_norm[(d+2)%self.dim] * q[2] + x_norm[(d+3)%self.dim] * q[3]
            fractal_value += np.sum(np.sin(rotated_x * scale * period) ** 2)
        
        # Adaptive gradient field with spectral filtering
        grad_field = 0.0
        for i in range(self.dim):
            # Dynamic modulation based on position and dimension
            mod_freq = 1 + self.adaptivity_factor * np.sin(i * 0.7)
            mod_amp = 1 + 0.6 * np.cos(i * 0.4)
            # Apply spectral filtering to gradient field
            filtered_x = x[i] * (1 + 0.1 * np.sin(3 * x[i]))
            grad_field += mod_amp * np.sin(filtered_x * mod_freq) * np.cos(filtered_x * mod_freq**2)
        
        # Multi-scale harmonic interference with chaotic phase modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            for k in range(1, min(8, self.dim + 3)):
                # Add chaotic phase component
                phase_mod = 1 + 0.2 * np.sin(k * x[i] * 0.3)
                harmonic_sum += (1/k) * np.sin(k * x[i] * phase_mod) * np.cos(k * x[i] * phase_mod * 0.7)
        
        # Asymmetric potential wells with varying depth and chaotic tunneling
        potential_well = 0.0
        for i in range(self.dim):
            # Create asymmetric basins using polynomial, exponential and chaotic terms
            well_term = (x[i]**3 + 0.5 * x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
            # Add chaotic tunneling component
            tunneling = 0.1 * np.sin(10 * x[i]) * np.cos(5 * x[i])
            potential_well += well_term + tunneling
        
        # Global scaling factor with fractal dimension influence and chaos parameter
        dim_scaling = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.5)
        
        # Combine all components with chaotic weighting
        chaos_weight = 0.5 + 0.3 * np.sin(np.sum(x) * 0.2)
        total_value = dim_scaling * (0.25 * fractal_value + 0.35 * grad_field + 
                                   0.2 * harmonic_sum + 0.2 * potential_well) * chaos_weight
        
        return total_value