import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate fractal chaotic sequence with self-similar properties
        self.fractal_seq = np.zeros(dim)
        x = 0.5
        for i in range(dim):
            x = 4 * x * (1 - x)
            self.fractal_seq[i] = x
            
        # Precompute dynamic phase shifts for each dimension
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, dim)
        
        # Precompute adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal radial basis functions with dynamic widths
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.fractal_seq[i])**2)
            width = 0.01 * (1 + 0.5 * np.sin(self.fractal_seq[i] * 10))
            rbfs[i] = np.exp(-dist / (2 * width**2))
        
        # Multi-scale chaotic interaction terms
        chaotic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            chaotic_terms[i] = np.sin(self.fractal_seq[i] * x_norm[i] * 5) * np.cos(self.fractal_seq[i] * x_norm[i] * 3)
        
        # Adaptive conditioning based on input magnitude
        conditioning = np.sum(self.conditioning_factors * np.abs(x_norm)**1.5)
        
        # Dynamic phase-shifted polynomial interactions
        poly_interaction = np.sum(np.sin(x_norm * self.phase_shifts) * np.cos(x_norm * self.phase_shifts * 2))
        
        # Self-similar noise with multiple scales
        noise = 0.0
        for scale in [0.1, 0.3, 0.7]:
            noise += scale * np.sum(np.sin(x_norm / scale) * np.random.uniform(0.5, 1.5, self.dim))
            
        # Sharp multi-modal transitions with fractal characteristics
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * 2)) > 0.8)
        
        # Combine all components with fractal weights
        total = 0.25 * np.sum(rbfs) + 0.25 * np.sum(chaotic_terms) + 0.2 * conditioning + 0.15 * poly_interaction + 0.15 * transitions + 0.05 * noise
        
        # Add fractal scaling factor for global conditioning
        fractal_scale = 1 + 0.5 * np.sin(np.sum(x_norm**3))
        
        return total * fractal_scale