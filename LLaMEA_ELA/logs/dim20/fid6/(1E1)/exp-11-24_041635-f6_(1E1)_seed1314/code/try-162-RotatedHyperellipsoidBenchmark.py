import numpy as np

class RotatedHyperellipsoidBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrices and condition numbers for each dimension
        np.random.seed(42)  # For reproducibility
        self.rotations = []
        self.conditionings = []
        for _ in range(dim):
            # Random orthogonal matrix
            Q, _ = np.linalg.qr(np.random.randn(dim, dim))
            self.rotations.append(Q)
            # Condition number between 1 and 100
            self.conditionings.append(np.random.uniform(1.0, 100.0))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        for i in range(self.dim):
            # Apply rotation to the input vector
            rotated_x = self.rotations[i] @ x
            
            # Compute quadratic form with adaptive conditioning
            quad_form = np.sum((rotated_x ** 2) * self.conditionings[i])
            
            # Add interaction terms between dimensions
            interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction += np.sin(x[i]) * np.cos(x[j]) * (1.0 + 0.1 * abs(x[i] - x[j]))
            
            # Combine components with a nonlinear transformation
            result += quad_form + 0.5 * interaction + 0.1 * np.sin(2.0 * x[i])
        
        # Add a global sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        global_mod = np.sin(0.3 * r) * np.exp(-0.02 * r)
        
        return result + global_mod