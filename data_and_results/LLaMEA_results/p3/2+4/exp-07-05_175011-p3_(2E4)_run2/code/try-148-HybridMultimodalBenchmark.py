import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees for conditioning
        poly_base = np.sum((x_norm ** 3) + 0.5 * (x_norm ** 2) + 0.1 * x_norm)
        
        # Radial basis function component with multiple centers
        rb_centers = np.linspace(-1, 1, min(5, self.dim))
        rb_sum = 0.0
        for i in range(len(rb_centers)):
            if i < self.dim:
                rb_sum += np.exp(-5 * (x_norm[i] - rb_centers[i%len(rb_centers)])**2)
        
        # Trigonometric mixture with varying frequencies and amplitudes
        trig_sum = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 2
            trig_sum += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * (1 + 0.3 * np.sin(3 * x_norm[i]))
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Coupling terms between variables with nonlinear interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling += (x_norm[i] * x_norm[j]) * np.sin(5 * (x_norm[i] - x_norm[j]))
        
        # Multi-modal component with shifted peaks and varying heights
        modal = 0.0
        peak_positions = np.linspace(-1, 1, 7)
        for pos in peak_positions:
            modal += np.exp(-20 * (x_norm - pos)**2) * (1 + 0.5 * np.sin(10 * pos))
        
        # Global optimum perturbation with chaotic-like behavior
        chaotic = np.sum(np.sin(10 * x_norm) * np.cos(15 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Combine all components with adaptive weights
        return cond_factor * (0.7 * poly_base + 1.2 * rb_sum + 0.9 * trig_sum + 0.6 * coupling + 1.5 * modal + 0.8 * chaotic)