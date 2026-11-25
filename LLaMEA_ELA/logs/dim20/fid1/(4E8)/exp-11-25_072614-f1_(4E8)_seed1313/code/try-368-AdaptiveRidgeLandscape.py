import numpy as np

class AdaptiveRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive ridge parameters
        self.ridge_count = 3 + int(np.random.rand() * 4)
        self.ridge_widths = 0.5 + np.random.rand(self.ridge_count) * 2.0
        self.ridge_heights = 1.0 + np.random.rand(self.ridge_count) * 3.0
        self.ridge_angles = np.random.rand(self.ridge_count) * 2 * np.pi
        self.curvature_adaptation = 0.5 + np.random.rand() * 2.0
        self.connectivity_strength = 0.3 + np.random.rand() * 1.2
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Multi-ridge structure with adaptive widths and heights
        for i in range(self.ridge_count):
            # Ridge direction vector
            ridge_dir = np.array([np.cos(self.ridge_angles[i]), np.sin(self.ridge_angles[i])])
            
            # Project point onto ridge direction
            proj = np.dot(x, ridge_dir)
            
            # Ridge function with adaptive width and height
            ridge_val = self.ridge_heights[i] * np.exp(-0.5 * (proj / self.ridge_widths[i])**2)
            result += ridge_val
            
        # Dynamic curvature component that adapts based on position
        curvature_term = 0.0
        for i in range(self.dim):
            # Adaptive curvature based on distance from center
            dist_from_center = np.abs(x[i])
            adaptive_curvature = self.curvature_adaptation * (1.0 + 0.5 * np.sin(dist_from_center))
            curvature_term += adaptive_curvature * x[i]**2
            
        # Connectivity and basin interaction terms
        connectivity_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                connectivity_term += self.connectivity_strength * np.exp(-distance**2 / 2.0)
                
        # Add noise component for additional complexity
        noise = np.random.rand() * 0.1
        
        # Combine all components
        result = result + curvature_term * 0.5 + connectivity_term * 0.3 + noise
        
        return result