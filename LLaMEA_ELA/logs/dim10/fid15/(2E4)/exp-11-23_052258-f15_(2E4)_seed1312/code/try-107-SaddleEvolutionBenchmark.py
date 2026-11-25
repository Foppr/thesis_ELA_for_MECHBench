import numpy as np

class SaddleEvolutionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute evolutionary parameters
        self.evolution_factors = [0.5 + 0.5 * np.sin(i * 0.7) for i in range(dim)]
        self.penalty_weights = [1.0 + 0.3 * np.cos(i * 0.4) for i in range(dim)]
        self.saddle_positions = [np.sin(i * 0.6) * 2.0 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Saddle-point structure component
        saddle_term = 0.0
        for i in range(self.dim):
            # Create saddle points at specific locations
            saddle_pos = self.saddle_positions[i % len(self.saddle_positions)]
            saddle_term += (x[i] - saddle_pos)**2 * (x[i] + saddle_pos)**2
            
        # Evolutionary gradient adaptation
        evolve_term = 0.0
        for i in range(self.dim):
            # Dynamic adaptation based on position and evolution factor
            evol_factor = self.evolution_factors[i % len(self.evolution_factors)]
            evolve_term += evol_factor * np.sin(2 * x[i]) * np.cos(3 * x[i])
            
        # Multi-scale penalty mechanism with dynamic weights
        penalty_term = 0.0
        for i in range(self.dim):
            # Apply different penalty types based on position and weight
            penalty_weight = self.penalty_weights[i % len(self.penalty_weights)]
            if x[i] > 0:
                penalty_term += penalty_weight * (x[i]**3 + 0.5 * np.sin(10 * x[i]))
            else:
                penalty_term += penalty_weight * (x[i]**4 + 0.3 * np.cos(8 * x[i]))
                
        # Cross-dimensional coupling with non-linear interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                cross_term += np.tanh(x[i] + x[j]) * (x[i]**2 + x[j]**2)
                
        # High-order polynomial component for complex curvature
        poly_term = 0.0
        for i in range(self.dim):
            # Use higher order terms to create complex landscape
            poly_term += (x[i]**5 - 2 * x[i]**3 + x[i]) * np.cos(0.5 * x[i])
            
        # Asymmetric gradient flow with time-dependent adaptation
        asym_term = 0.0
        for i in range(self.dim):
            # Create asymmetric behavior using sine and cosine
            asym_factor = 1.0 + 0.2 * np.sin(i * 0.3)
            asym_term += asym_factor * np.sin(4 * x[i]) * np.cos(2 * x[i])
            
        # Combine all terms with dimension-dependent scaling
        weights = [0.3, 0.25, 0.2, 0.15, 0.1]
        total = (weights[0] * saddle_term + 
                weights[1] * evolve_term + 
                weights[2] * penalty_term + 
                weights[3] * cross_term + 
                weights[4] * asym_term)
                
        # Add dynamic global scaling based on landscape complexity
        scale = 1.0 + 0.15 * np.log(self.dim + 1) + 0.02 * np.sum(np.abs(x)) + 0.01 * np.sum(x**2)
        
        return scale * total