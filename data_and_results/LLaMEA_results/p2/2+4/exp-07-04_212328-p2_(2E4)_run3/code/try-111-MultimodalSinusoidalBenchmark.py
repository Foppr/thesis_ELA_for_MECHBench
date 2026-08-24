import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add chaotic sinusoidal radial basis functions with fractal-like structure
        rbf_sum = 0
        for i in range(20):
            # Fractal-like center distribution
            angle = i * 0.43 + np.sin(i * 0.2) * 0.3
            radius = 4.0 + 0.5 * np.sin(i * 0.7) * np.cos(i * 0.5)
            center = np.array([radius * np.sin(angle), radius * np.cos(angle)])
            
            if self.dim >= 2:
                diff = x[:2] - center
                # Adaptive variance based on position
                variance = 0.3 + 0.2 * np.sin(x[0] * 0.5) * np.cos(x[1] * 0.3)
                rbf_sum += np.exp(-0.5 * np.sum(diff**2) / variance)
        
        f += 3.0 * rbf_sum
        
        # Add multi-scale chaotic sinusoidal modulation
        mod_sum = 0
        for i in range(self.dim):
            # Nested chaotic modulation with multiple frequencies
            mod1 = np.sin(x[i] * (1 + 0.5 * np.sin(x[i] * 0.3)))
            mod2 = np.cos(x[i] * (1 + 0.3 * np.cos(x[i] * 0.2)))
            mod3 = np.sin(x[i] * (1 + 0.2 * np.sin(x[i] * 0.7)))
            mod_sum += mod1 * mod2 * mod3
            
        f += 1.2 * mod_sum
        
        # Add fractal-like coupling with self-similar patterns
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Limited coupling for complexity control
                # Self-similar amplitude modulation
                amp = 0.8 + 0.4 * np.sin(x[i] * 0.5) * np.cos(x[j] * 0.4)
                coupling_sum += amp * np.sin(x[i] * x[j] * 0.8 + 0.3 * np.sin(x[i] + x[j]))
                
        f += 1.8 * coupling_sum
        
        # Add recursive chaotic phase interactions
        phase_sum = 0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] + np.sin(x[i] * 1.5) + np.sin(x[i] * 0.7) + np.sin(x[i] * 0.3))
        f += 0.9 * np.sin(phase_sum * 3.0)
        
        # Add polynomial chaos with higher-order non-linear coupling
        poly_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Higher order polynomial terms
                poly_sum += (x[i]**4 + x[j]**4) * np.sin(x[i] * x[j] * 0.5)
        f += 0.6 * poly_sum
        
        # Add multiple nested global minima with varying scales and positions
        minima_positions = []
        for i in range(15):
            # Nested structure with different scales
            scale = 1.0 + 0.3 * np.sin(i * 0.5)
            angle = i * 0.8 + np.cos(i * 0.3) * 0.2
            radius = 2.0 * scale + 0.5 * np.sin(i * 0.7)
            minima_positions.append([radius * np.sin(angle), radius * np.cos(angle)])
            
        minima_sum = 0
        for pos in minima_positions:
            if self.dim >= len(pos):
                diff = x[:len(pos)] - np.array(pos)
                # Varying depth for minima
                depth = 0.5 + 0.3 * np.sin(pos[0] * 0.3)
                minima_sum += depth * np.exp(-0.2 * np.sum(diff**2))
        f += 2.0 * minima_sum
        
        # Add fractal noise with chaotic pattern
        noise = 0
        for i in range(self.dim):
            # Fractal noise with multiple scales
            noise += np.sin(x[i] * 15.0 + np.sin(x[i] * 11.0) + np.sin(x[i] * 7.0)) * np.cos(x[i] * 8.0)
        f += 0.15 * noise
        
        # Add dimensional coupling with chaotic interaction strength
        coupling_strength = 0.5 + 0.3 * np.sin(np.sum(x) * 0.2)
        f += coupling_strength * np.sum(np.sin(x) * np.cos(x * 0.5))
        
        return f