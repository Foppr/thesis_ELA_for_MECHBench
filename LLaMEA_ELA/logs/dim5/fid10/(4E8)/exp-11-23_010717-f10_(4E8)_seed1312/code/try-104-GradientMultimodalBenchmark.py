import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Radial symmetry term with adaptive curvature
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 * (1.0 + 0.3 * np.sin(5.0 * r))
        
        # Saddle-point dominance with multiple competing optima
        saddle_terms = 0.0
        for i in range(self.dim):
            saddle_terms += (0.8 * x[i]**2 * np.cos(3.0 * x[i]) + 
                           0.4 * x[i]**4 * np.sin(2.0 * x[i]) + 
                           0.2 * np.sin(7.0 * x[i]) * np.cos(5.0 * x[i]))
        
        # Adaptive curvature term with varying condition numbers
        curvature = 0.0
        for i in range(self.dim):
            # Slightly modified curvature coefficients and frequencies
            curv = 1.0 + 0.6 * np.sin(0.4 * i)  # Increased variation
            curvature += curv * x[i]**2 * (1.0 + 0.3 * np.cos(4.0 * x[i]))  # Adjusted coefficient
        
        # Enhanced cross-dimensional coupling with modified interaction strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased interaction strength and changed frequency
                strength = 0.4 + 0.3 * np.sin(0.3 * (i + j))  # Higher base strength
                coupling += strength * x[i] * x[j] * np.sin(3.0 * (x[i] + x[j]))  # Changed frequency
        
        # Multi-modal component with increased complexity
        modal_term = 0.0
        for i in range(self.dim):
            # Added higher frequency terms and adjusted coefficients
            modal_term += (3.5 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + 
                          2.5 * np.sin(5.0 * x[i])**2 + 
                          1.8 * np.cos(4.0 * x[i])**2 +
                          0.5 * np.sin(8.0 * x[i]) * np.cos(6.0 * x[i]))  # Added new term
        
        # Global scaling factor with modified variance
        scale = 1.0 + 0.15 * np.sum(np.sin(x)**2)  # Increased scaling
        
        # Penalty for being far from origin to encourage convergence
        penalty = 0.07 * r**3  # Increased penalty strength
        
        return scale * (radial_term + saddle_terms + curvature + coupling + modal_term) + penalty