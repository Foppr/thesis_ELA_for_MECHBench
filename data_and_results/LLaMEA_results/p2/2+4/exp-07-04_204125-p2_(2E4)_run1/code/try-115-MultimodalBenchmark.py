import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Separable quadratic terms with varying condition numbers
        for i in range(self.dim):
            # Varying weights to create conditioning differences
            weight = 1.0 + 0.5 * np.sin(i * 0.7)
            result += 0.5 * weight * x[i]**2
        
        # Non-separable helix-like chaotic structure with rotational coupling
        helix_component = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            # Create helix-like coupling between adjacent variables
            helix_term = np.sin(3.0 * x[i]) * np.cos(3.0 * x[j]) + \
                         np.cos(3.0 * x[i]) * np.sin(3.0 * x[j])
            helix_component += helix_term * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        result += 0.8 * helix_component
        
        # Add directional bias through sinusoidal modulation
        bias_component = 0.0
        for i in range(self.dim):
            # Directional bias based on variable position
            bias_term = np.sin(2.0 * x[i] + i * 0.5) * np.cos(1.5 * x[i] + i * 0.3)
            bias_component += bias_term
        
        result += 0.6 * bias_component
        
        # Introduce rotational complexity with cross-term interactions
        rotation_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Rotational coupling with angle-dependent weights
                angle = np.arctan2(x[j], x[i])
                rotation_term = np.sin(2.0 * angle) * x[i] * x[j]
                rotation_component += rotation_term * np.exp(-0.05 * (i + j))
        
        result += 0.4 * rotation_component
        
        # Add fractal-like perturbations with varying frequencies
        fractal_component = 0.0
        for i in range(self.dim):
            # Multi-scale fractal perturbation
            fractal_term = np.sin(10.0 * x[i]) * np.cos(5.0 * x[i]) + \
                          np.sin(20.0 * x[i]) * np.cos(10.0 * x[i]) + \
                          np.sin(40.0 * x[i]) * np.cos(20.0 * x[i])
            fractal_component += fractal_term * np.exp(-0.2 * x[i]**2)
        
        result += 0.3 * fractal_component
        
        # Add dimensionality-dependent scaling
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result