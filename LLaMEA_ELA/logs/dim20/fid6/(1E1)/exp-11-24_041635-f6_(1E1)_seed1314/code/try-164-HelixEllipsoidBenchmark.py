import numpy as np

class HelixEllipsoidBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Helical arrangement of ellipsoids
        helix_term = 0.0
        num_ellipsoids = min(15, self.dim)
        
        for i in range(num_ellipsoids):
            # Create a helical path in the first two dimensions
            angle = i * 0.4
            radius = 1.0 + i * 0.2
            center_x = radius * np.cos(angle)
            center_y = radius * np.sin(angle)
            
            # Ellipsoid parameters with varying condition numbers
            a = 1.0 + i * 0.3
            b = 1.0 + i * 0.4
            
            # Rotate coordinates for ellipsoid orientation
            rot_angle = i * 0.2
            cos_a = np.cos(rot_angle)
            sin_a = np.sin(rot_angle)
            
            if self.dim >= 2:
                x_rot = (x[0] - center_x) * cos_a + (x[1] - center_y) * sin_a
                y_rot = -(x[0] - center_x) * sin_a + (x[1] - center_y) * cos_a
                
                # Ellipsoid function with varying condition number
                ellipsoid_value = a * x_rot**2 + b * y_rot**2
                helix_term += np.exp(-0.1 * i) * ellipsoid_value
            
            # Additional dimensions with rotated ellipsoids
            if self.dim > 2:
                for d in range(2, min(self.dim, num_ellipsoids)):
                    if i < self.dim:
                        # Simple quadratic term in higher dimensions
                        ellipsoid_value = (x[d] - i * 0.3)**2
                        helix_term += np.exp(-0.05 * i) * ellipsoid_value
        
        # Chaotic sine wave modulation
        chaotic_modulation = 0.0
        r = np.sqrt(np.sum(x**2))
        
        for i in range(self.dim):
            freq = 1.0 + i * 0.7
            amp = 1.0 / (1.0 + i * 0.3)
            chaotic_modulation += amp * np.sin(freq * x[i] + np.sin(freq * r))
        
        # Combine components with different weights
        result = helix_term + 0.5 * chaotic_modulation
        
        return result