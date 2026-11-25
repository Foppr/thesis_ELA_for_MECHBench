import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate rotation matrices for each dimension
        self.rotations = []
        for _ in range(dim):
            angle = np.random.uniform(0, 2 * np.pi)
            rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            self.rotations.append(rot)
        
        # Saddle point parameters
        self.saddle_centers = np.random.uniform(-3.0, 3.0, dim)
        self.saddle_strengths = np.random.uniform(0.5, 2.0, dim)
        
        # Chaotic perturbation parameters
        self.perturbation_magnitudes = np.random.uniform(0.1, 0.5, dim)
        self.perturbation_frequencies = np.random.uniform(0.5, 2.0, dim)
        
        # Basin parameters for ellipsoidal structure
        self.basin_axes = np.random.uniform(1.0, 3.0, dim)
        self.basin_centers = np.random.uniform(-2.0, 2.0, dim)
        
        # Global scaling and noise parameters
        self.global_scale = np.random.uniform(0.5, 2.0)
        self.noise_level = np.random.uniform(0.01, 0.1)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        fitness = 0.0
        
        for i in range(self.dim):
            # Ellipsoidal basin component
            basin_term = ((x[i] - self.basin_centers[i]) / self.basin_axes[i])**2
            
            # Saddle point component
            saddle_term = (x[i] - self.saddle_centers[i])**2 * self.saddle_strengths[i]
            
            # Chaotic perturbation with modified nonlinear term
            chaotic_perturbation = self.perturbation_magnitudes[i] * np.sin(
                self.perturbation_frequencies[i] * x[i] + 
                np.random.uniform(0, 2*np.pi)
            ) * np.cos(x[i] * 0.5)  # Added cosine modulation for increased nonlinearity
            
            # Combine all terms with rotation for cross-dimensional interactions
            if i < len(self.rotations) - 1:
                # Apply rotation between dimensions with enhanced coupling strength
                rotated_val = self.rotations[i].dot(np.array([x[i], x[i+1]]))
                cross_term = (rotated_val[0] - rotated_val[1])**2 * 0.3  # Increased coupling
            else:
                cross_term = 0.0
            
            # Add a quadratic interaction term for additional complexity
            if i > 0:
                quadratic_interaction = 0.1 * (x[i] - x[i-1])**2
                
            else:
                quadratic_interaction = 0.0
            
            # Combine all components for this dimension
            fitness += basin_term + saddle_term + chaotic_perturbation + cross_term + quadratic_interaction
        
        # Apply global scaling and add noise
        fitness = fitness * self.global_scale
        noise = np.random.uniform(-self.noise_level, self.noise_level)
        return fitness + noise