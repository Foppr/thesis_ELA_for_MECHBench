import numpy as np

class ChaoticLogisticPotentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        self.bifurcation_control = np.random.uniform(0.1, 0.9, dim)
        self.interference_strengths = np.random.uniform(0.5, 2.0, (dim, dim))
        # Potential well parameters
        self.well_depths = np.random.uniform(1.0, 5.0, dim)
        self.well_positions = np.random.uniform(-4.0, 4.0, dim)
        self.well_widths = np.random.uniform(0.5, 2.0, dim)
        # Cross-dimensional coupling
        self.coupling_phase_shifts = np.random.uniform(0, 2*np.pi, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map components with bifurcation control
        chaotic_terms = 0.0
        for i in range(self.dim):
            r = self.r_params[i] * (1 + self.bifurcation_control[i] * np.sin(x_norm[i]))
            x_prev = x_norm[i]
            # Iterate logistic map 10 times to reach chaotic regime
            for _ in range(10):
                x_prev = r * x_prev * (1 - x_prev)
            chaotic_terms += x_prev
        
        # Cross-dimensional interference patterns
        interference_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interference_terms += (self.interference_strengths[i, j] * 
                                        np.sin(x_norm[i] + x_norm[j] + self.coupling_phase_shifts[i, j]))
        
        # Energy-like potential wells
        potential_terms = 0.0
        for i in range(self.dim):
            distance = x_norm[i] - self.well_positions[i]
            potential_terms += (self.well_depths[i] * 
                              np.exp(-0.5 * (distance**2) / (self.well_widths[i]**2)))
        
        # Add a global scaling factor to control overall landscape complexity
        scaling_factor = 1.0 + 0.5 * np.sin(np.sum(x_norm))
        
        # Combine all terms with optimized weights
        return (0.4 * chaotic_terms + 
                0.3 * interference_terms + 
                0.25 * potential_terms + 
                0.05 * scaling_factor)