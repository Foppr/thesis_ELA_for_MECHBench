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
                a, b = 1.0 + i * 0.2, 1.0 + (i + 1) * 0.2
                term = (rotated[0] / a)**2 + (rotated[1] / b)**4
                
                # Add chaotic modulation with modified frequencies
                chaos = np.sin(20 * rotated[0]) * np.cos(15 * rotated[1])
                
                result += term + 0.5 * chaos
        
        # Additional chaotic sinusoidal components with altered amplitudes and frequencies
        for i in range(self.dim):
            freq = 4.0 + i * 0.5
            amp = 0.7 + i * 0.08
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.9)
        
        # Add a global sinusoidal modulation based on the entire vector with modified parameters
        r = np.sqrt(np.sum(x**2))
        global_mod = np.sin(0.5 * r) * np.cos(0.4 * r) * np.exp(-0.08 * r)
        result += 0.5 * global_mod
        
        # Add a term that creates many local minima through irregular oscillations with modified coefficients
        irregular = 0.0
        for i in range(self.dim):
            irregular += np.sin(25 * x[i]) * np.cos(20 * x[i]) * (1.0 + 0.2 * x[i]**2)
        result += 0.4 * irregular
        
        # Add stronger cross-term interactions to increase conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * x[i] * x[j] * np.sin(7 * (x[i] + x[j]))
        
        # Add a high-frequency chaotic component that increases complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(50 * x[i]) * np.cos(40 * x[i])
        result += 0.6 * high_freq
        
        # Add a multi-scale sinusoidal modulation to increase landscape complexity
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i])
        result += 0.3 * multi_scale
        
        return result