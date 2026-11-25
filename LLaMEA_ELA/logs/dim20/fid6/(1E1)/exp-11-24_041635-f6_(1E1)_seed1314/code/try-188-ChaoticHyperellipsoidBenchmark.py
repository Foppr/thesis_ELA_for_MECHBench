import numpy as np

class ChaoticHyperellipsoidBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrices for different subspaces
        self.rotations = []
        for i in range(0, dim, 2):
            if i + 1 < dim:
                angle = np.pi * (i / dim)
                c, s = np.cos(angle), np.sin(angle)
                self.rotations.append(np.array([[c, -s], [s, c]]))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperellipsoid components with rotation
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Extract 2D subspace
                xi = x[i:i+2]
                
                # Apply rotation
                rotated = self.rotations[(i // 2) % len(self.rotations)] @ xi
                
                # Hyperellipsoid term with varying exponents
                a, b = 1.0 + i * 0.15, 1.0 + (i + 1) * 0.15
                term = (rotated[0] / a)**2 + (rotated[1] / b)**3
                
                # Add chaotic modulation with modified frequencies
                chaos = np.sin(15 * rotated[0]) * np.cos(10 * rotated[1])
                
                result += term + 0.4 * chaos
        
        # Additional chaotic sinusoidal components with altered amplitudes
        for i in range(self.dim):
            freq = 3.0 + i * 0.4
            amp = 0.6 + i * 0.07
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        
        # Add a global sinusoidal modulation based on the entire vector with modified parameters
        r = np.sqrt(np.sum(x**2))
        global_mod = np.sin(0.4 * r) * np.cos(0.3 * r) * np.exp(-0.06 * r)
        result += 0.4 * global_mod
        
        # Add a term that creates many local minima through irregular oscillations with modified coefficients
        irregular = 0.0
        for i in range(self.dim):
            irregular += np.sin(20 * x[i]) * np.cos(15 * x[i]) * (1.0 + 0.15 * x[i]**2)
        result += 0.3 * irregular
        
        # Add cross-term interactions to increase conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * x[i] * x[j] * np.sin(5 * (x[i] + x[j]))
        
        return result