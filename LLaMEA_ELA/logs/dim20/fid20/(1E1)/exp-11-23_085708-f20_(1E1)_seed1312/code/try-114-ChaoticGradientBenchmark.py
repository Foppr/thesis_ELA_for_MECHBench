import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Polynomial radial component with chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r**3 + 0.5 * r**4 + 0.1 * np.sin(10 * r) * np.cos(7 * r)
        
        # Chaotic gradient modulation using logistic map-like behavior
        grad_mod = 1.0
        for i in range(self.dim):
            # Logistic map inspired chaotic component
            chaos_val = np.sin(x[i] * 2) * np.cos(x[i] * 3) + 0.5 * np.sin(x[i] * 7)
            grad_mod *= (1 + 0.3 * chaos_val * np.exp(-0.1 * x[i]**2))
            
        # Polynomial interaction terms with varying exponents
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create saddle-point behavior with mixed polynomial and trigonometric terms
                poly_interaction = (x[i]**2 + x[j]**2) * (x[i] * x[j])**0.5
                trig_interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                interaction_term += 0.1 * (poly_interaction + trig_interaction) * (i + j + 1)
                
        # Multimodal component with multiple polynomial peaks
        multi_modal = 0.0
        for i in range(self.dim):
            # Create multiple local minima using different polynomial bases
            multi_modal += (x[i]**4 - 2 * x[i]**2 + 0.5 * np.sin(5 * x[i]) + 
                           0.3 * np.cos(3 * x[i]) + 0.1 * np.sin(9 * x[i]))
            
        # Saddle-point structure with alternating positive and negative curvature
        saddle_term = 0.0
        for i in range(self.dim):
            # Create alternating hessian behavior
            saddle_term += (-1)**i * (x[i]**3 - 3 * x[i]) * np.cos(0.5 * x[i])
            
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (np.exp(-0.5 * (x[i] - x[j])**2) * 
                                 np.sin(0.3 * (x[i] + x[j])) * (i + j + 1))
                
        # Global scaling factor with chaotic modulation
        global_scale = 1.0 + 0.2 * np.sin(np.sum(x_scaled**2)) * np.cos(np.sum(x_scaled))
        
        # Combine all terms
        result = radial_term + grad_mod * multi_modal + interaction_term + saddle_term + cross_coupling + global_scale
        
        return result