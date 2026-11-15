import numpy as np

class FractalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base polynomial with conditioning
        f = 0.5 * np.sum(x**4) + 0.3 * np.sum(x**2)
        
        # Recursive fractal-like structure using polynomial compositions
        for i in range(self.dim):
            # Nested polynomial with increasing complexity
            poly_val = x[i]
            for depth in range(1, 5):
                poly_val = poly_val**2 + 0.5 * np.sin(poly_val * depth)
            f += 0.8 * poly_val
            
        # Chaotic phase interactions with non-linear coupling
        phase_sum = 0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * (i + 1) * 0.7) * np.cos(x[i] * (i + 1) * 0.3)
        f += 0.6 * np.sin(phase_sum * 5)
        
        # Multi-scale polynomial interactions with varying exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Varying polynomial exponents for complexity
                exp_i = 2 + 0.5 * np.sin(i * 0.5)
                exp_j = 2 + 0.5 * np.cos(j * 0.5)
                f += 0.3 * (x[i]**exp_i + x[j]**exp_j) * np.sin(x[i] * x[j])
                
        # Discontinuous gradient terrain with step functions
        for i in range(self.dim):
            step_val = np.floor(np.sin(x[i] * 3) * 2) + 1
            f += 0.4 * step_val * np.abs(x[i] - 0.5 * step_val)
            
        # Recursive self-similar pattern with polynomial scaling
        for i in range(self.dim):
            # Create fractal-like behavior with recursive scaling
            scaled_x = x[i] * 0.5
            for scale in range(1, 4):
                scaled_x = scaled_x**2 + 0.3 * np.sin(scaled_x * scale)
            f += 0.2 * scaled_x
            
        # High-frequency oscillatory components with varying amplitudes
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(i * 0.3)
            amp = 1.5 + 0.5 * np.cos(i * 0.7)
            f += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Multi-modal structure with non-uniform valley depths
        valleys = []
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                valleys.append((x[i], x[i+1]))
        
        valley_term = 0
        for i, (xi, yi) in enumerate(valleys):
            # Create valleys with different depths and positions
            depth = 0.8 + 0.4 * np.sin(i * 0.5)
            pos_x = -2.5 + 5 * np.sin(i * 0.3)
            pos_y = -2.5 + 5 * np.cos(i * 0.4)
            dist = np.sqrt((xi - pos_x)**2 + (yi - pos_y)**2)
            valley_term += depth * np.exp(-dist**2 * 0.5)
        f += 1.2 * valley_term
        
        # Add discontinuous jump terms to increase gradient complexity
        jump_term = 0
        for i in range(self.dim):
            jump_val = np.floor(x[i] * 2) * 0.5
            jump_term += np.abs(x[i] - jump_val) * np.sin(x[i] * 10)
        f += 0.5 * jump_term
        
        # Add final chaotic modulation with recursive structure
        final_mod = 0
        for i in range(self.dim):
            temp = x[i]
            for _ in range(3):
                temp = np.sin(temp * 3) + 0.2 * np.cos(temp * 2)
            final_mod += temp
        f += 0.3 * np.sin(final_mod * 7)
        
        return f