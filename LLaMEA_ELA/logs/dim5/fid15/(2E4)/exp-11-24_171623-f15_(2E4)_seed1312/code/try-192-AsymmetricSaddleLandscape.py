import numpy as np

class AsymmetricSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute directional scaling factors
        self.scales = np.array([1.0 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)])
        # Precompute rotation angles for anisotropic structure
        self.angles = np.array([0.1 * i * np.pi / dim for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Saddle point components with asymmetric weights
        saddle_sum = 0.0
        for i in range(self.dim):
            # Asymmetric cubic potential with directional scaling
            if x_norm[i] < 0:
                saddle_sum += self.scales[i] * (x_norm[i]**3 + 0.3 * x_norm[i]**2)
            else:
                saddle_sum += self.scales[i] * (x_norm[i]**3 - 0.3 * x_norm[i]**2)
        
        # Anisotropic elliptic structure with directional rotation
        elliptic_sum = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            # Rotated quadratic form with varying eccentricity
            xi_rot = x_norm[i] * np.cos(self.angles[i]) - x_norm[j] * np.sin(self.angles[i])
            xj_rot = x_norm[i] * np.sin(self.angles[i]) + x_norm[j] * np.cos(self.angles[i])
            elliptic_sum += 0.5 * (xi_rot**2 + 0.3 * xj_rot**2)
        
        # Implicit constraint boundaries with exponential penalty
        constraint_sum = 0.0
        for i in range(self.dim):
            # Create soft boundaries at ±1 with increasing penalty
            dist_from_boundary = 1.0 - np.abs(x_norm[i])
            if dist_from_boundary < 0:
                constraint_sum += np.exp(-dist_from_boundary * 5.0)
        
        # Cross-dimensional coupling with exponential interaction
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Exponentially decaying interaction with directional preference
                dist = np.abs(x_norm[i] - x_norm[j])
                interaction = np.exp(-dist * 2.0) * (x_norm[i] * x_norm[j])
                cross_sum += interaction * (1.0 + 0.1 * np.sin(i * j))
        
        # Sharp gradient transition regions with piecewise linear components
        sharp_sum = 0.0
        for i in range(self.dim):
            # Create steep transitions at specific thresholds
            if x_norm[i] < -0.5:
                sharp_sum += 2.0 * (x_norm[i] + 0.5)**2
            elif x_norm[i] > 0.5:
                sharp_sum += 2.0 * (x_norm[i] - 0.5)**2
            else:
                sharp_sum += 0.1 * x_norm[i]**4
        
        # Combine components with adaptive weights
        result = 0.3 * saddle_sum + 0.25 * elliptic_sum + 0.2 * constraint_sum + 0.15 * cross_sum + 0.1 * sharp_sum
        
        # Add dimensionality-dependent conditioning factor
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.1 * np.abs(x_norm[i]) + 0.05 * x_norm[i]**2)
        
        return result * condition_factor