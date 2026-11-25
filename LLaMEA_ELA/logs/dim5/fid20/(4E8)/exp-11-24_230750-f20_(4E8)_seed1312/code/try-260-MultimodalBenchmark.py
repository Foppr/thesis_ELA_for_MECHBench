import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with dynamic coefficients
        chaos = 0.0
        for i in range(self.dim):
            # Dynamic coefficient based on position and dimension
            coeff = 1.0 + 0.3 * np.sin(0.5 * (i + 1) * np.sum(x))
            # Polynomial terms with varying exponents
            poly_term = coeff * (x[i]**4 - 2*x[i]**2 + 1)
            chaos += poly_term
        
        # Dynamic hyperbolic tangent oscillations with varying frequencies
        tanh_osc = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * (i + 1) * np.sum(x))
            # Hyperbolic tangent oscillation with amplitude modulation
            amp = 1.0 + 0.2 * np.cos(0.4 * x[i])
            tanh_osc += amp * np.tanh(freq * x[i]) * np.sin(0.7 * x[i])
        
        # Adaptive radial basis function component with time-varying centers
        rbf = 0.0
        num_centers = min(5, self.dim)
        for i in range(num_centers):
            # Dynamic center position
            center = 2.0 * np.sin(0.4 * (i + 1) * np.sum(x))
            # Time-varying width parameter
            width = 0.5 + 0.3 * np.cos(0.2 * (i + 1) * np.sum(x))
            # Radial basis function
            rbf += np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Cross-dimensional coupling with dynamic weights
        coupling = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Dynamic weight based on sum of all variables
                weight = 0.8 + 0.2 * np.sin(0.6 * np.sum(x))
                coupling += weight * (x[i] * x[(i+1) % self.dim]) * np.cos(0.3 * (x[i] + x[(i+1) % self.dim]))
        
        # Asymmetric gradient deception component
        deception = 0.0
        for i in range(self.dim):
            # Asymmetric penalty that increases near boundaries
            penalty = 2.0 * np.exp(-0.1 * (x[i] - 5.0)**2) if x[i] > 4.0 else 0.0
            penalty += 2.0 * np.exp(-0.1 * (x[i] + 5.0)**2) if x[i] < -4.0 else 0.0
            # Deceptive term that misleads gradient-based methods
            deception += penalty + 0.5 * np.sin(3 * x[i]) * np.cos(2 * x[i])
        
        # Combine all components with adaptive weights
        total = (0.3 * chaos + 
                0.25 * tanh_osc + 
                0.2 * rbf + 
                0.15 * coupling + 
                0.1 * deception)
        
        return total