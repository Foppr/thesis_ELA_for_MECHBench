import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal chaotic sequence with higher dimensionality
        self.fractal_seq = np.array([0.5])
        for i in range(dim * 50):
            next_val = 4 * self.fractal_seq[-1] * (1 - self.fractal_seq[-1])
            self.fractal_seq = np.append(self.fractal_seq, next_val)
        self.fractal_seq = self.fractal_seq[:dim]
        
        # Precompute hybrid polynomial coefficients with varying degrees
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, dim)
        self.poly_degrees = np.random.randint(3, 10, dim)
        
        # Precompute RBF centers and widths for multi-scale interaction
        self.rbf_centers = np.random.uniform(-1.0, 1.0, (dim, 3))
        self.rbf_widths = np.random.uniform(0.01, 0.2, 3)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-scale radial basis functions with fractal scaling
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(3):
                dist = np.sum((x_norm - self.rbf_centers[i, j])**2)
                rbf_sum += np.exp(-dist / (2 * self.rbf_widths[j]**2))
            rbfs[i] = rbf_sum
        
        # Fractal chaotic interaction using multiple logistic maps
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(self.fractal_seq[i] * x_norm[i]) * np.cos(self.fractal_seq[i] * 2 * x_norm[i])
        
        # Hybrid polynomial interactions with dynamic exponents
        poly_interaction = 0
        for i in range(self.dim):
            poly_interaction += self.poly_coeffs[i] * (x_norm[i]**self.poly_degrees[i] + 0.5 * x_norm[i]**(self.poly_degrees[i] + 1))
        
        # Dynamic noise with fractal correlation
        noise = 0
        for i in range(self.dim):
            noise += np.abs(x_norm[i]) * np.random.normal(0.5, 0.3) * (1 + 0.2 * np.sin(self.fractal_seq[i] * 10))
        
        # Sharp multi-modal transitions with fractal boundary conditions
        transitions = 0
        for i in range(self.dim):
            transitions += np.abs(np.sin(x_norm[i] * np.pi * 3)) > 0.8
        
        # Combine all components with adaptive weights
        total = 0.25 * np.sum(rbfs) + 0.35 * chaotic + 0.2 * noise + 0.15 * poly_interaction + 0.05 * transitions
        
        # Add fractal global scaling factor
        fractal_scale = 1 + 0.8 * np.sin(np.sum(x_norm**3))
        
        return total * fractal_scale