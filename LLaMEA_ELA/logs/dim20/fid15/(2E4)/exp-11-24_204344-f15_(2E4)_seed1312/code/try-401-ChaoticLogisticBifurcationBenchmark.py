import numpy as np

class ChaoticLogisticBifurcationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        self.initial_conditions = np.random.uniform(0.1, 0.9, dim)
        self.bifurcation_points = np.random.uniform(2.5, 4.0, dim)
        # Spectral coupling matrix
        self.coupling_kernel = np.random.normal(0, 0.5, (dim, dim))
        # Frequency modulation factors
        self.frequency_modulators = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.array(x)
        result = 0.0
        
        # Chaotic logistic map components
        for i in range(self.dim):
            r = self.r_values[i]
            x_i = self.initial_conditions[i]
            
            # Iterate logistic map for several steps to reach chaotic regime
            for _ in range(20):
                x_i = r * x_i * (1 - x_i)
            
            # Apply bifurcation modulation
            bif_point = self.bifurcation_points[i]
            modulated_r = r * (1.0 + 0.2 * np.sin(x[i] * self.frequency_modulators[i]))
            
            # Compute chaotic contribution
            chaotic_val = modulated_r * x_i * (1 - x_i)
            result += chaotic_val * np.cos(x[i] * 3.0) * 0.5
            
        # Cross-dimensional spectral coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    kernel_val = self.coupling_kernel[i, j]
                    coupling_term += kernel_val * np.sin(x[i] - x[j]) * (1.0 + 0.1 * np.abs(x[i] - x[j]))
        
        result += 0.3 * coupling_term
        
        # Add harmonic interference and global scaling
        harmonic_component = np.sum(np.sin(x * 2.0) * np.cos(x * 1.5))
        global_scale = np.sum(x**2) * 0.05
        
        return result + harmonic_component + global_scale