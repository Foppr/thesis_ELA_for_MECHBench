import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sinusoidal component with time-varying parameters
        sin_component = 0
        for i in range(self.dim):
            freq = 1.0 + 4.0 * np.sin(0.3 * i + 2.0 * np.cos(0.7 * i))
            amp = 2.0 + np.sin(0.5 * i) * np.cos(0.2 * i)
            phase = 0.5 * np.sin(0.4 * i) * np.cos(0.6 * i)
            sin_component += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] / 3.0)
        
        # Dynamic radial basis function with chaotic center positions and adaptive variances
        rbf_component = 0
        for i in range(self.dim):
            center = -4.5 + 9.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5) + 0.5 * np.sin(1.2 * i)
            variance = 0.3 + 0.7 * np.abs(np.sin(0.8 * i))
            rbf_component += 4.0 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Multi-scale directional gradient coupling with chaotic interaction weights
        grad_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(4.0 * dx) * np.cos(2.5 * dx)
                weight = 1.0 + 0.3 * np.sin(0.9 * i + 0.6 * j)
                grad_coupling += weight * (dx**2 + dy**2) / (1.0 + np.abs(dx) + np.abs(dy))
        
        # Polynomial modulation with chaotic coefficients and higher-order terms
        poly_mod = 0
        for i in range(self.dim):
            coeff1 = 0.8 + 0.4 * np.sin(1.5 * i)
            coeff2 = 1.2 + 0.3 * np.cos(0.7 * i)
            coeff3 = 0.6 + 0.4 * np.sin(0.9 * i)
            poly_mod += coeff1 * x[i]**5 - coeff2 * x[i]**4 + coeff3 * x[i]**3
        
        # Cross-dimensional interaction terms with noise injection
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(2.0 * (x[i] + x[j])) * np.cos(1.5 * (x[i] - x[j]))
                noise = 0.1 * np.random.normal(0, 1)
                cross_term += interaction * noise
        
        # Dimensionality-dependent conditioning factor with chaotic scaling
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.2 * np.sin(0.5 * self.dim)
        
        # Combine all components with dynamic weights and chaos injection
        total = (3.0 * sin_component + 4.0 * rbf_component + 0.5 * grad_coupling + 
                0.7 * poly_mod + 40.0 * condition_factor + 2.0 * cross_term)
        
        # Add chaotic perturbation to increase landscape complexity
        chaos_perturb = 0.5 * np.sin(10.0 * np.sum(x)) * np.cos(8.0 * np.prod(x))
        
        return total + chaos_perturb