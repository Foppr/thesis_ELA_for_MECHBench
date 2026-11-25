import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - pulls towards origin with stronger influence
        basin = 0.2 * np.sum(x**2)
        
        # Grid of global minima terms with enhanced frequencies and amplitudes
        grid_minima = 0.0
        for i in range(self.dim):
            # Enhanced trigonometric pattern with varied coefficients
            grid_minima += 3.5 * np.sin(1.7 * x[i]) * np.cos(1.2 * x[i]) + \
                          1.0 * np.sin(2.8 * x[i]) * np.cos(2.0 * x[i]) + \
                          0.5 * np.sin(3.2 * x[i]) * np.cos(2.5 * x[i])
            
        # Add interactive cross-terms with higher interaction strength and different pattern
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased complexity through nonlinear cross-interactions with mixed terms
                cross_terms += 0.8 * np.sin(1.2 * x[i]) * np.cos(1.2 * x[j]) + \
                              0.4 * np.cos(1.5 * x[i]) * np.sin(1.5 * x[j]) + \
                              0.3 * np.sin(1.0 * x[i]) * np.sin(1.0 * x[j])
        
        # Add a small noise term to increase challenge but reduce overfitting
        noise = 0.015 * np.sum(np.sin(7.0 * x) * np.cos(5.0 * x))
        
        # Add a cubic term for additional nonlinearity and better gradient behavior
        cubic_term = 0.06 * np.sum(x**3)
        
        # Add a quartic term to increase the complexity of the landscape
        quartic_term = 0.02 * np.sum(x**4)
        
        # Add a logarithmic barrier near the boundaries to prevent out-of-bounds evaluation
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.8:
                boundary_penalty += 10.0 * (abs(x[i]) - 4.8)**2
                
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + boundary_penalty