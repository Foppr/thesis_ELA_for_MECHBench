import numpy as np

class HierarchicalPolynomialChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize hierarchical polynomial chaos parameters
        self.poly_orders = np.random.randint(3, 8, dim)
        self.correlation_lengths = np.random.uniform(0.5, 3.0, dim)
        self.adaptivity_params = np.random.uniform(0.1, 2.0, dim)
        self.shape_parameters = np.random.uniform(0.5, 2.5, dim)
        self.hierarchy_levels = min(4, max(2, dim // 3))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hierarchical polynomial chaos expansion with adaptive dimensionality
        chaos_sum = 0.0
        for i in range(self.dim):
            # Adaptive polynomial basis functions
            poly_basis = np.zeros(self.poly_orders[i])
            for j in range(self.poly_orders[i]):
                if j == 0:
                    poly_basis[j] = 1.0
                elif j == 1:
                    poly_basis[j] = x_norm[i]
                else:
                    # Chebyshev polynomial recurrence relation
                    poly_basis[j] = 2 * x_norm[i] * poly_basis[j-1] - poly_basis[j-2]
            
            # Adaptive weighting based on dimensionality
            adaptive_weight = self.adaptivity_params[i] * np.exp(-0.1 * i)
            chaos_sum += adaptive_weight * np.sum(poly_basis**2)
        
        # Dynamic fitness shaping with multi-scale correlation structure
        correlation_terms = 0.0
        for i in range(self.dim):
            # Multi-scale correlation with varying lengths
            scale_factor = self.correlation_lengths[i]
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x_norm[i] - x_norm[j])
                corr_term = np.exp(-dist**2 / (2 * scale_factor**2))
                correlation_terms += corr_term * np.sin(dist * np.pi)
        
        # Hierarchical dimensionality reduction with dynamic weighting
        reduction_terms = 0.0
        for level in range(self.hierarchy_levels):
            start_idx = int(level * self.dim / self.hierarchy_levels)
            end_idx = int((level + 1) * self.dim / self.hierarchy_levels)
            if end_idx > start_idx:
                level_vars = x_norm[start_idx:end_idx]
                # Dynamic reduction based on variance
                var_reduction = np.var(level_vars)
                reduction_terms += var_reduction * np.exp(-level * 0.5)
        
        # Shape parameter modulation for fitness landscape ruggedness
        shape_modulation = 0.0
        for i in range(self.dim):
            mod_factor = self.shape_parameters[i]
            shape_modulation += (np.sin(x_norm[i] * mod_factor) * 
                               np.cos(x_norm[i] * mod_factor * 0.7) * 
                               np.exp(-x_norm[i]**2 / 2))
        
        # Multi-modal component with dynamic peaks
        modal_terms = 0.0
        num_peaks = max(3, self.dim // 2)
        for peak in range(num_peaks):
            peak_center = np.random.uniform(-1, 1, self.dim)
            peak_height = np.random.uniform(0.5, 2.0)
            dist = np.sum((x_norm - peak_center)**2)
            modal_terms += peak_height * np.exp(-dist / (2 * 0.3**2))
        
        # Combined fitness function with proper weighting
        return (0.4 * chaos_sum + 
                0.3 * correlation_terms + 
                0.15 * reduction_terms + 
                0.1 * shape_modulation + 
                0.05 * modal_terms)