import numpy as np

class HelicalMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with periodic oscillations
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sin(3 * r) * np.exp(-0.1 * r**2)
        
        # Helical structure in higher dimensions
        helix = 0.0
        if self.dim >= 2:
            # Create helical pattern using sine and cosine combinations
            for i in range(self.dim - 1):
                helix += np.sin(5 * np.pi * x_scaled[i]) * np.cos(5 * np.pi * x_scaled[i+1])
        
        # Cross-dimensional coupling with periodic terms
        coupling = 0.0
        if self.dim >= 3:
            for i in range(self.dim - 2):
                coupling += np.sin(4 * np.pi * (x_scaled[i] + x_scaled[i+1])) * \
                          np.cos(3 * np.pi * (x_scaled[i+1] + x_scaled[i+2]))
        
        # Periodic multimodal component
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(7 * np.pi * x_scaled[i]) * np.cos(6 * np.pi * x_scaled[i]) + \
                       0.5 * np.sin(11 * np.pi * x_scaled[i]) * np.cos(9 * np.pi * x_scaled[i])
        
        # Add a central peak with radial decay
        center_peak = np.exp(-2 * r**2) * (1 + 0.3 * np.sin(8 * r))
        
        # Combine all components with different weights
        return 0.3 * radial + 0.4 * helix + 0.2 * coupling + 0.05 * periodic + 0.05 * center_peak