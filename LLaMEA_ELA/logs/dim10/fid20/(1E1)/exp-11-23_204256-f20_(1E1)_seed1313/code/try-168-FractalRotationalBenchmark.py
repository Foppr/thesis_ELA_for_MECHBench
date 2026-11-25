import numpy as np

class FractalRotationalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal radial component with multiple self-similar scales
        r = np.sqrt(np.sum(x_norm**2))
        fractal_radial = np.sum([
            0.5**i * np.sin(2**(i+1) * np.pi * r) * np.exp(-r**2 / (2 * 0.5**i**2))
            for i in range(1, min(6, self.dim + 1))
        ])
        
        # Quaternion-inspired rotational component
        if self.dim >= 4:
            # Use first four dimensions for quaternion-like rotation
            q = x_norm[:4]
            q_norm = np.sqrt(np.sum(q**2))
            if q_norm > 1e-8:
                q_unit = q / q_norm
                rot_component = (
                    np.sin(10 * q_norm) * np.cos(8 * q_norm) * 
                    (q_unit[0]**2 + q_unit[1]**2 - q_unit[2]**2 - q_unit[3]**2)
                )
            else:
                rot_component = 0
        else:
            rot_component = 0
            
        # Multi-scale cross-dimensional coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for scalability
                dist = np.abs(x_norm[i] - x_norm[j])
                cross += (
                    np.exp(-dist**2) * np.sin(15 * (x_norm[i]**2 + x_norm[j]**2)) *
                    np.cos(12 * (x_norm[i]**3 + x_norm[j]**3)) +
                    0.7 * np.exp(-dist**3) * np.sin(10 * (x_norm[i]**4 + x_norm[j]**4)) *
                    np.cos(8 * (x_norm[i]**5 + x_norm[j]**5))
                )
        
        # Adaptive conditioning based on dimensionality
        cond = 1.0 + 2.0 * np.log(self.dim + 1)
        
        # Combined fitness with fractal and rotational elements
        return cond * (fractal_radial + rot_component + cross + 
                      0.3 * np.sin(50 * r) * np.cos(40 * r))